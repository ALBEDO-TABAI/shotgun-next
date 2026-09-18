#!/usr/bin/env python3
"""Create three original symbolic music exercises; no audio is rendered.

Python 3.10+, standard library only.
    python generate_midi.py --output-dir ./midi_output
C4 = MIDI 60. All variants share tempo, harmony, bass and MIDI programs.
The generated files are parsed again to check notes, timing and differences.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import struct
from collections import Counter
from pathlib import Path

PPQ = 480
BPM = 118
TEMPO_US = round(60_000_000 / BPM)
END_TICK = 16 * PPQ
# (quarter-note offset, MIDI pitch, duration in quarter notes)
MELODY = [
    (0.5, 78, 0.5), (1, 81, 1), (2, 76, 1),
    (4.5, 78, 0.5), (5, 81, 1), (6, 83, 1),
    (8, 79, 0.5), (8.5, 78, 0.5), (9, 76, 1), (10, 71, 1),
    (12, 76, 1), (13, 78, 1), (14, 74, 2),
]
CHORDS = [[57, 62, 64, 66], [55, 59, 62, 66],
          [55, 59, 62, 64], [57, 59, 64, 66]]
BASS = [38, 38, 40, 38]


def vlq(value: int) -> bytes:
    """Encode the MIDI variable-length integer used for delta times."""
    if not 0 <= value <= 0x0FFFFFFF:
        raise ValueError(f"Invalid MIDI variable-length value: {value}")
    buf = [value & 0x7F]
    value >>= 7
    while value:
        buf.append((value & 0x7F) | 0x80)
        value >>= 7
    return bytes(reversed(buf))


def meta(kind: int, payload: bytes) -> bytes:
    return bytes([0xFF, kind]) + vlq(len(payload)) + payload


def track(events: list[tuple[int, int, bytes]]) -> bytes:
    """Serialize absolute-tick events; note-offs precede note-ons at a tick."""
    events = list(events) + [(END_TICK, 99, meta(0x2F, b""))]
    data = bytearray()
    previous = 0
    for tick, _, message in sorted(events, key=lambda e: (e[0], e[1])):
        if not previous <= tick <= END_TICK:
            raise ValueError("Event outside the four-bar exercise")
        data.extend(vlq(tick - previous))
        data.extend(message)
        previous = tick
    return b"MTrk" + struct.pack(">I", len(data)) + bytes(data)


def note_track(name: str, channel: int, program: int, velocity: int,
               notes: list[tuple[float, int, float]]) -> bytes:
    events = [(0, 0, meta(0x03, name.encode("ascii"))),
              (0, 1, bytes([0xC0 | channel, program]))]
    for start, pitch, duration in notes:
        on = round(start * PPQ)
        off = round((start + duration) * PPQ)
        if not (0 <= pitch <= 127 and 0 < velocity <= 127 and on < off <= END_TICK):
            raise ValueError("Invalid note")
        events.append((on, 3, bytes([0x90 | channel, pitch, velocity])))
        events.append((off, 2, bytes([0x80 | channel, pitch, 0])))
    return track(events)


def build(melody: list[tuple[float, int, float]]) -> bytes:
    events = [(0, 0, meta(0x03, b"118 BPM / four-bar exercise")),
              (0, 1, meta(0x51, TEMPO_US.to_bytes(3, "big"))),
              (0, 2, meta(0x58, bytes([4, 2, 24, 8]))),
              (0, 3, meta(0x59, bytes([2, 0])))]
    for bar in range(4):
        events.append((bar * 4 * PPQ, 4, meta(0x06, f"Bar {bar+1}".encode())))
    harmony = [(bar * 4, pitch, 4) for bar, chord in enumerate(CHORDS) for pitch in chord]
    bass = [(bar * 4, pitch, 4) for bar, pitch in enumerate(BASS)]
    # Programs are zero-based GM values, merely neutral playback placeholders.
    tracks = [track(events),
              note_track("Melody", 0, 0, 70, melody),
              note_track("Harmony", 1, 4, 48, harmony),
              note_track("Bass", 2, 32, 58, bass)]
    return b"MThd" + struct.pack(">IHHH", 6, 1, len(tracks), PPQ) + b"".join(tracks)


def decode_vlq(data: bytes, offset: int) -> tuple[int, int]:
    value = 0
    for _ in range(4):
        if offset >= len(data):
            raise ValueError("Truncated variable-length value")
        byte = data[offset]
        offset += 1
        value = (value << 7) | (byte & 0x7F)
        if byte < 0x80:
            return value, offset
    raise ValueError("Overlong variable-length value")


def parse_generated_file(path: Path) -> dict:
    """Independent readback for this script's explicit-status MIDI subset.

    This is not a general MIDI importer; it deliberately rejects running status
    and event types the writer does not use, rather than silently skipping them.
    """
    data = path.read_bytes()
    if len(data) < 14 or data[:4] != b"MThd":
        raise ValueError("Missing MIDI header")
    length, fmt, count, division = struct.unpack(">IHHH", data[4:14])
    if (length, fmt, count, division) != (6, 1, 4, PPQ):
        raise ValueError("Unexpected MIDI header")
    offset, notes, endpoints, tempos = 14, [], [], []
    program_changes = []
    for track_index in range(count):
        if data[offset:offset + 4] != b"MTrk":
            raise ValueError("Missing track chunk")
        size = int.from_bytes(data[offset+4:offset+8], "big")
        payload = data[offset+8:offset+8+size]
        if len(payload) != size:
            raise ValueError("Truncated track")
        offset += 8 + size
        cursor, tick, ended = 0, 0, False
        active: dict[tuple[int, int], tuple[int, int]] = {}
        while cursor < len(payload):
            delta, cursor = decode_vlq(payload, cursor)
            tick += delta
            status = payload[cursor]
            cursor += 1
            if status == 0xFF:
                kind = payload[cursor]
                cursor += 1
                size2, cursor = decode_vlq(payload, cursor)
                value = payload[cursor:cursor + size2]
                if len(value) != size2:
                    raise ValueError("Truncated metadata")
                cursor += size2
                if kind == 0x51:
                    tempos.append((tick, int.from_bytes(value, "big")))
                elif kind == 0x2F:
                    if size2 != 0 or cursor != len(payload) or active:
                        raise ValueError("Bad end event or hanging notes")
                    ended = True
            elif 0x80 <= status <= 0xEF:
                kind, channel = status & 0xF0, status & 0x0F
                if kind == 0xC0:
                    program_changes.append((track_index, channel, payload[cursor]))
                    cursor += 1
                elif kind in (0x80, 0x90):
                    pitch, velocity = payload[cursor:cursor+2]
                    cursor += 2
                    key = channel, pitch
                    if kind == 0x90 and velocity:
                        if key in active:
                            raise ValueError("Unexpected overlapping same-pitch notes")
                        active[key] = (tick, velocity)
                    else:
                        if key not in active:
                            raise ValueError("Note-off without note-on")
                        start, attack_velocity = active.pop(key)
                        if tick <= start:
                            raise ValueError("Non-positive note length")
                        notes.append((track_index, channel, pitch, start,
                                      tick-start, attack_velocity))
                else:
                    raise ValueError(f"Unexpected status {status:02x}")
            else:
                raise ValueError("Unsupported or invalid status")
        if not ended or tick != END_TICK:
            raise ValueError("Incorrect track end")
        endpoints.append(tick)
    if offset != len(data) or tempos != [(0, TEMPO_US)]:
        raise ValueError("Unexpected trailing data or tempo map")
    return {"notes": sorted(notes), "track_end_ticks": endpoints,
            "programs": program_changes, "tempo_us_per_quarter": TEMPO_US}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    variants = {
        "01_motif_base.mid": list(MELODY),
        "02_motif_vo_space.mid": [n for n in MELODY if not 4 <= n[0] < 12],
        "03_motif_open_ending.mid": [(s, 76 if s == 14 else p, d) for s, p, d in MELODY],
    }
    parsed = {}
    for name, melody in variants.items():
        path = args.output_dir / name
        path.write_bytes(build(melody))
        parsed[name] = parse_generated_file(path)
        expected = sorted((1, 0, p, round(s*PPQ), round(d*PPQ), 70) for s, p, d in melody)
        actual = [n for n in parsed[name]["notes"] if n[0] == 1]
        if actual != expected:
            raise ValueError("Readback melody differs from the intended exercise")
    a, b, c = [parsed[n] for n in variants]
    for other in (b, c):
        if [n for n in a["notes"] if n[0] > 1] != [n for n in other["notes"] if n[0] > 1]:
            raise ValueError("An accompaniment changed between variants")
        if a["programs"] != other["programs"]:
            raise ValueError("Program changes differ between variants")
    if len(a["notes"]) != 33 or len(b["notes"]) != 26 or len(c["notes"]) != 33:
        raise ValueError("Unexpected note counts")
    if set(a["notes"]) - set(c["notes"]) != {(1, 0, 74, 14*PPQ, 2*PPQ, 70)}:
        raise ValueError("Unexpected deleted note in ending variant")
    if set(c["notes"]) - set(a["notes"]) != {(1, 0, 76, 14*PPQ, 2*PPQ, 70)}:
        raise ValueError("Unexpected added note in ending variant")
    report = {
        "scope": "symbolic MIDI format/timing/note comparison only; no audio rendering, DAW import or listening test",
        "format": 1, "tracks": 4, "ticks_per_quarter": PPQ,
        "requested_bpm": BPM, "encoded_tempo_us_per_quarter": TEMPO_US,
        "realized_bpm": 60_000_000/TEMPO_US,
        "quarter_notes": 16, "duration_seconds": 16*TEMPO_US/1_000_000,
        "all_track_end_ticks": a["track_end_ticks"],
        "checks": {"balanced_note_events": True, "four_bar_length": True,
                   "matching_accompaniment_and_programs": True,
                   "vo_variant_omits_only_middle_two_bars_melody": True,
                   "ending_variant_changes_only_final_pitch": True},
        "files": [{"name": n, "note_count": len(parsed[n]["notes"]),
                   "notes_by_track": dict(Counter(str(note[0]) for note in parsed[n]["notes"])),
                   "sha256": hashlib.sha256((args.output_dir/n).read_bytes()).hexdigest()}
                  for n in variants],
    }
    (args.output_dir / "validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

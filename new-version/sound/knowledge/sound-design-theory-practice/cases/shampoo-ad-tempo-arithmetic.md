---
type: Case Study
title: "洗发水广告案例 · 固定 118 BPM 的时间计算与复算代码"
description: "118 BPM、4/4 下一小节=120/59≈2.034 秒；3 秒入口+12 小节有拍结构（至≈27.407 秒）+≈2.593 秒收束窗口；以精确分数计算并附 Python 复算片段，计算只验证数学不验证听感。"
tags: [topic-07, 案例, 洗发水广告, BPM, 时间计算, 代码]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/sound/声音设计理论与方法_二至十/07_洗发水广告_完整声音设计案例.md#6. 时间计算：30 秒不自然等于整数个 4/4 小节"
---

> 证据身份：**教学假设案例**。方向词来自对话；30 秒、4/4、118 BPM、旁白窗口等均为本篇假设；无真实影片、音频、试听或授权。

# 计算（四分音符为一拍，固定 118 BPM）
```text
一拍时长 = 60 / 118 = 30 / 59 ≈ 0.508474576 秒
一小节时长 = 4 × 30 / 59 = 120 / 59 ≈ 2.033898305 秒
12 小节 = 48 拍 = 1440 / 59 ≈ 24.406779661 秒
明确音乐拍点起始 = 3.000000000 秒
12 小节结束 = 3 + 1440 / 59 ≈ 27.406779661 秒
到 30 秒剩余尾部 = 153 / 59 ≈ 2.593220339 秒
```

# 分配
- 3 秒声音入口（可已有来自物体的音高材料，但不标为已建立主拍）；
- 12 小节有拍结构；
- ≈2.593 秒收束窗口——**不要求**持续 2.593 秒混响，可先让音乐短尾完成再留少量空间，或由产品现实声与短动机共同收束。

# 纪律
- 数值按**分数**计算，小数是派生显示值。
- 片长、音乐起点或拍单位改变后应**重算**，不手动修补各行使其表面相加。

# Examples：复算代码（§25，仅标准库）
```python
from fractions import Fraction
bpm = 118; beats_per_bar = 4
music_start = Fraction(3, 1); film_end = Fraction(30, 1)
bar_seconds = Fraction(60 * beats_per_bar, bpm)
# 每段使用的小节数分别为 2、2、3、3、2，共十二小节
bars_by_cue = [("C02", 2), ("C03", 2), ("C04", 3), ("C05", 3), ("C06", 2)]
cursor = music_start
intervals = [("C01", Fraction(0), music_start)]
for cue_id, bars in bars_by_cue:
    end = cursor + bars * bar_seconds
    intervals.append((cue_id, cursor, end)); cursor = end
assert cursor <= film_end, "音乐主体超出片长，需重新设计。"
intervals.append(("C07", cursor, film_end))
assert all(a < b for _, a, b in intervals)
assert all(intervals[i][2] == intervals[i + 1][1] for i in range(len(intervals) - 1))
for cue_id, start, end in intervals:
    print(cue_id, f"{float(start):.3f}", f"{float(end):.3f}")
```
代码不读取或生成音频，不替代实际剪辑的帧率与拍点核对；速度改变、弱起或表演时值偏离都需反映在真实节奏映射里。

# 关系
- 上位主题：[07 洗发水广告完整案例](/topics/07-shampoo-ad-case.md)
- 产出：[核心段落表](/cases/shampoo-ad-cue-segment-table.md)
- 秒／帧／小节映射：[帧量化与拍点同步](/principles/frame-quantization-vs-beat-sync.md)
- 时间表示与片长／乐句协商的通用方法：[05 声音时间线](/topics/05-sound-timeline.md)

# Citations
[1] [07 篇 §6、§25](../../../声音设计理论与方法_二至十/07_洗发水广告_完整声音设计案例.md)

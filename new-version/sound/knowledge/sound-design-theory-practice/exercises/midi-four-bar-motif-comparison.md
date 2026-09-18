---
type: Exercise
title: "四小节 MIDI 对照练习：把“怎么改”变成具体音符差异"
description: "三个 118 BPM、4/4、四轨 MIDI：基础版、删除第 2–3 小节领奏的旁白留白版、仅把末音 D5 改为 E5 的句末变化版；伴奏与程序号完全相同，只做符号层验证，未渲染音频、未试听。"
resource: ../../../声音创作与制作_实践知识包/exercises/
tags: [practice-exercise, MIDI, 动机, 旁白空间, 句末, 单变量对照]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/sound/声音创作与制作_实践知识包/exercises/README.md"
files:
  - ../../../声音创作与制作_实践知识包/exercises/01_motif_base.mid
  - ../../../声音创作与制作_实践知识包/exercises/02_motif_vo_space.mid
  - ../../../声音创作与制作_实践知识包/exercises/03_motif_open_ending.mid
  - ../../../声音创作与制作_实践知识包/exercises/generate_midi.py
  - ../../../声音创作与制作_实践知识包/exercises/validation.json
---

> 证据身份：**原创教学材料**（对应主文 §3.3、§3.4）。不是已试听通过的配乐，也不是 30 秒成片音轨。

# 三个版本
| 文件 | 只改变什么 | 比较问题 |
|---|---|---|
| [01_motif_base.mid](../../../声音创作与制作_实践知识包/exercises/01_motif_base.mid) | 基础四小节旋律、和声与低音 | 认识原句与休止位置 |
| [02_motif_vo_space.mid](../../../声音创作与制作_实践知识包/exercises/02_motif_vo_space.mid) | 删除第 2、3 小节领奏，其余不变 | 不靠整条音乐降音量，能否获得人声空间？ |
| [03_motif_open_ending.mid](../../../声音创作与制作_实践知识包/exercises/03_motif_open_ending.mid) | 仅把最后的 D5 改为 E5 | 相同和声与音色下，句末音改变了怎样的结束感？ |

文件名"open ending"只是待测方向，**不保证**听众感到"开放"；02 版并未加入旁白。

# Schema：符号规格
| 项 | 值 |
|---|---|
| 拍号／长度 | 4/4，四小节 = 16 个四分音符 |
| 目标速度 | 118 BPM（编码 508475 µs／四分音符 → 实际 ≈117.999901667 BPM） |
| 时长 | **8.135600 s**（理想 118 BPM 为 8.135593220 s，差约 6.78 µs）；不含音源释放尾音 |
| 格式 | MIDI format 1，480 ticks/quarter，4 轨（1 条元数据轨 + 3 条乐音轨），全部终止于 tick 7680 |
| 音高记法 | 科学音高 C4 = MIDI 60；软件八度名可能不同，以 MIDI 编号为准 |
| 调号元事件 | 2 个升号 |

| 轨道 | 通道（从 1 计） | GM 程序号（从 0 计） | 固定力度 | 内容 |
|---|---:|---:|---:|---|
| Melody | 1 | 0（钢琴占位） | 70 | 13 个音（基础版） |
| Harmony | 2 | 4（电钢琴占位） | 48 | 每小节一个四音和弦，共 16 音 |
| Bass | 3 | 32（低音占位） | 58 | D2 D2 E2 D2，共 4 音 |

程序号只是播放占位；比较时须自行保持相同音源与设置。无随机时差、表情控制器或音频处理。

# 音符内容（据 generate_midi.py）
- 旋律（拍位, MIDI 音高, 时值）：第 1 小节 F#5 A5 E5；第 2 小节 F#5 A5 B5；第 3 小节 G5 F#5 E5 B4；第 4 小节 E5 F#5 **D5（2 拍）**。
- 和声：A3-D4-E4-F#4 ｜ G3-B3-D4-F#4 ｜ G3-B3-D4-E4 ｜ A3-B3-E4-F#4。
- 02 版：删除拍位 4–12 内的 7 个旋律音 → 旋律 6 音；03 版：末音 74 (D5) → 76 (E5)。

# 验证结果（validation.json）
| 文件 | 音符数 | 各轨 (Mel/Har/Bass) |
|---|---:|---|
| 01_motif_base | 33 | 13 / 16 / 4 |
| 02_motif_vo_space | 26 | 6 / 16 / 4 |
| 03_motif_open_ending | 33 | 13 / 16 / 4 |

检查全部通过：note-on/off 配对平衡、四小节长度、伴奏与程序号一致、02 版只删中间两小节旋律、03 版只改末音音高。文件 SHA-256 记录于 validation.json。

**验证边界**：只覆盖符号层的 MIDI 格式、时间与音符对照；**不包括** DAW 导入、音频渲染、监听设备或审美试听。"符号写对"不等于"音乐好听"。

# 练习步骤
1. 三个文件放进同一个 DAW 工程，确认拍速与音源一致（部分软件导入时需选择是否采用文件速度）。
2. 听基础版：第 1、2 小节保留了什么共同材料？
3. 比较 02 版的中段留白；再**加上自己的旁白或节奏相近的临时话语**，检查是否仍太密或失去连贯。
4. 比较 01 与 03：**不能先告诉试听者"开放"再把回答当独立验证**。
5. 完成音符对照后，再尝试移调、换音色、改发音与演奏表情——每次明确当前比较的变量；不要同时换音色、升音量、改旋律再归因于一个音符。

可复算：`python generate_midi.py --output-dir ./midi_output`（Python 3.10+ 标准库）。

# 关系
- 上位主题：[实践包主枢纽](/topics/p-sound-creation-production.md)
- 主文 §3.3 的音符写作过程（本练习的来源材料）：[四小节动机练习](/exercises/four-bar-motif-d-center-118bpm.md)；和声变化速度对照：[和声节奏 A/B/C 对照](/exercises/harmonic-rhythm-abc-comparison.md)
- 在贯穿案例中的使用：[A 三个决定](/cases/practice-shampoo-three-decisions.md)、[C 先写四小节](/cases/practice-shampoo-four-bar-to-draft.md)
- 单变量比较的原则与限度：[诊断比较与方案比较](/frameworks/diagnostic-vs-solution-comparison.md)
- 02 版对应的规则写法：[最小行动单元](/principles/minimum-action-unit-rule.md)
- 编配层替代混音避让：[侧链避让](/methods/sidechain-ducking-for-voiceover.md)
- 提问方式与命名影响：[09 声音评价与验收](/topics/09-sound-evaluation-acceptance.md)
- 学习路径第 1–2 步：[学习顺序](/methods/learning-order-small-works-first.md)

# Citations
[1] [练习说明 exercises/README.md](../../../声音创作与制作_实践知识包/exercises/README.md)
[2] [validation.json](../../../声音创作与制作_实践知识包/exercises/validation.json)
[3] [generate_midi.py](../../../声音创作与制作_实践知识包/exercises/generate_midi.py)
[4] [实践知识包 §3.3、§3.4](../../../声音创作与制作_实践知识包/声音创作与制作_实践知识包.md)

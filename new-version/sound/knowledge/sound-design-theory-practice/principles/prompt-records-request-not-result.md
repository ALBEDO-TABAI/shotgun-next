---
type: Principle
title: "提示词只记录请求，不证明实际结果"
description: "生成提示中的参数、\"真人演奏\"等只是请求；实际速度、来源、分轨需测量或人工确认后另行记录。"
tags: [topic-04, 生成式工具, 证据边界, 溯源]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/sound/声音设计理论与方法_二至十/04_声音描述语言_从感觉到执行.md#14. 三种 brief：面向导演、制作人员与生成系统"
---

# 原则
提示词是**请求记录**，不是**事实来源**。

# 具体表现
| 提示中写了 | 不能据此声明 | 需要的证据 |
|---|---|---|
| 118 BPM | 输出稳定为 118 BPM | 测量或人工确认 |
| 真实演奏／人性化 | 由真人演奏 | 素材来源记录 |
| 类似呼吸的声音 | 录音中有人呼吸 | 来源记录 |
| 时间码命令 | 已精确落实 | 实际审听位置 |
| 分轨（工具仅做分离估计） | 原始创作分轨 | 工具能力确认 |

# 应用
- 素材来源与听感**分开记录**。
- 检查顺序：目标是否清楚 → 描述是否自相矛盾 → 工具能否执行 → 实际音频。不要跳过前三步直接责怪模型"没有理解高级"。

# 关系
- 上位主题：[04 声音描述语言](/topics/04-sound-description-language.md)
- 出现位置：[三种 brief](/templates/three-audience-sound-briefs.md)、[发音与演奏行为](/frameworks/articulation-performance-behavior.md)
- 计划与实现分字段：[点位生产表](/templates/cue-production-sheet.md)
- 生成意图、真实素材与批准状态分开：[10 AI 影视团队声音协作](/topics/10-ai-team-sound-collaboration.md)

# Citations
[1] [04 声音描述语言 §8、§14、§16](../../../声音设计理论与方法_二至十/04_声音描述语言_从感觉到执行.md)

---
type: Skill Interface
title: "Skill：声音时间线（05）——最小闭环"
description: "声音点位设计的 skill 接口：输入当前剪辑与目标，输出点位表、交接说明、留白清单与待确认项，并通过入点理由、可感任务、尾部、语言保护、变更传播五项检验。"
tags: [topic-05, skill, spotting, 时间线]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/sound/声音设计理论与方法_二至十/05_声音时间线_入点出点留白与交接.md#16. 声音时间线 skill：最小闭环"
---

# 触发
- 决定哪里有音乐／哪里没有；安排进入、退出、留白与交接。
- 剪辑版本变化后需要更新声音时间线。
- 片长与乐句冲突；多部门争用同一时间窗口。

# 最小输入
- 当前剪辑、真实时长／帧率、声音目标、已有音乐与必要语言信息。
- **只有剧本时**：只能输出假设窗口，不能声称逐帧完成。

# 处理步骤
1. 标意义变化（[三个时钟](/frameworks/three-clocks-story-picture-music.md)、[四种触发](/frameworks/four-trigger-types.md)）。
2. 标硬动作与语言保护区（[三级同步](/frameworks/sync-anchor-three-levels.md)）。
3. 提出进入与退出理由（[入点三位置](/frameworks/entry-three-positions.md)、[出点与尾部](/frameworks/exit-modes-and-tail.md)）。
4. 设计主要交接（[音乐与人声交接](/methods/music-voice-handoff.md)、[声音桥接](/frameworks/sound-bridge-and-source-reveal.md)）。
5. 选择音乐结构与留白（[四种留白](/frameworks/four-kinds-of-silence.md)、[片长与乐句](/methods/fitting-length-to-phrases.md)）。
6. 最后处理秒／帧／小节映射（[单一权威时间基准](/frameworks/time-representation-seconds-frames-bars.md)）。
7. 节奏冲突时明确由画面、音乐还是局部声音调整，记录依据（[窗口冲突表](/templates/window-conflict-table.md)）。

# 输出
- 一张[点位表／生产表](/templates/cue-production-sheet.md)
- 一张全段前后景交接说明
- 一个留白清单
- 一个需确认的技术／版本列表

# 质量门禁
- 入点是否有理由；关键任务是否可感；尾部是否完整；语言是否受保护；变更是否传播到所有依赖（[剪辑变更重验](/methods/edit-change-revalidation.md)）。
- 过一遍[对抗性点位检查](/checklists/adversarial-cue-check.md)。
- 覆盖比例、计划时间、技术同步不作为艺术效果证据（[原则](/principles/music-coverage-ratio-not-quality-score.md)）。

# 核心知识段（精炼）
先识别故事、画面、音乐三个时钟，再决定进入、持续、退出与留白；每个关键点有事件／理解／状态／形式触发，区分文件起点、可感入口与任务显现；同步标为硬锚点、软窗口或自由区间；分别处理最后音头、主体结束、尾部与文件边界；多类声音共享前景交接规则；秒、帧、音乐位置由一个权威时间基准派生；剪辑变化后复核叙事理由、语言保护和素材依赖；无真实片源时只提假设窗口。

# 关系
- 上位主题：[05 声音时间线](/topics/05-sound-timeline.md)
- 讨论方法：[有效的点位讨论](/methods/effective-spotting-discussion.md)
- 上游：[04 声音描述语言](/topics/04-sound-description-language.md)；下游：[09 声音评价](/topics/09-sound-evaluation-acceptance.md)、[10 AI 影视团队声音协作](/topics/10-ai-team-sound-collaboration.md)

# Citations
[1] [05 声音时间线 §16、核心知识段](../../../声音设计理论与方法_二至十/05_声音时间线_入点出点留白与交接.md)

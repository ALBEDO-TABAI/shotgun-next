---
type: Template
title: "点位生产表：计划、实现与待验证分字段"
description: "从点位表到生产表的 16 个字段；计划与实测时间分开保存，明确当前批准版本；cue 表不替代版权申报。"
tags: [topic-05, 模板, cue sheet, 版本, 状态]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/sound/声音设计理论与方法_二至十/05_声音时间线_入点出点留白与交接.md#14. 从点位表到生产表：写清计划、实现与待验证"
---

# Schema
```text
cue_id：唯一段落标识
picture_revision：对应画面版本
task：本段主要任务
trigger：事件／理解／状态／形式变化
anchor_type：硬锚点／软窗口／自由区间
planned_start / planned_end：计划区间
entry_behavior：怎样成为可听前景
key_events：音头、动机完成、身份揭示、配器交接
exit_behavior：完成／中断／转化／移交
tail_policy：尾部是否越过段落；文件边界如何处理
foreground_handoff：前景从谁转给谁
protected_information：不能被破坏的信息或动作
implementation_asset：实际使用音频；未生成时为空
observed_start / observed_end：实际测得或审听位置
status：计划／候选／已审／已批准／需重验
unresolved：缺少的证据与下一动作
```

# 填写规则
- **计划时间与实际实现时间不覆盖同一字段**，否则看不出偏差。
- 不长期保留多个"最终起点"让下游自选；明确当前批准版本，历史计划仅作追溯。
- 可选补充字段（用于非线性材料）：所属事件、本次呈现用途（见 [非线性时间](/frameworks/nonlinear-time-recall-repetition.md)）。
- 此表**不是版权申报文件的自动替代物**：创作、资产来源与权利信息可以关联但用途不同。

# 关系
- 上位主题：[05 声音时间线](/topics/05-sound-timeline.md)
- 字段来源：[四种触发](/frameworks/four-trigger-types.md)、[三级同步](/frameworks/sync-anchor-three-levels.md)、[入点三位置](/frameworks/entry-three-positions.md)、[出点与尾部](/frameworks/exit-modes-and-tail.md)、[音乐与人声交接](/methods/music-voice-handoff.md)
- 时间字段的权威基准：[秒、帧与音乐位置](/frameworks/time-representation-seconds-frames-bars.md)
- 状态与批准、计划与素材分离：[10 AI 影视团队声音协作](/topics/10-ai-team-sound-collaboration.md)
- 权利对象：[COPY · 美国版权局说明](/references/copy.md)

# Citations
[1] [05 声音时间线 §14](../../../声音设计理论与方法_二至十/05_声音时间线_入点出点留白与交接.md)

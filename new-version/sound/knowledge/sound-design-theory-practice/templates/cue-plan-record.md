---
type: Template
title: "cue 计划记录（只记录计划、不冒充生产结果）"
description: "一条 cue 记录含 cue_id、时间线版本、时间基准、计划区间、任务、音乐与声音动作、依赖、资产 ID、生产状态、分维度评审和下一动作；计划阶段资产为空、评审为未审。"
tags: [topic-10, AI协作, cue, 记录, 时间线]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/sound/声音设计理论与方法_二至十/10_AI影视团队_声音协作与交付.md#7. 生成意图、真实素材与批准状态必须分开"
---

# Schema
| 字段 | 含义 |
|---|---|
| `cue_id` | 段落标识 |
| `timeline_revision` | 依赖的画面版本 |
| `time_basis` | 时间基准（引用权威时间线） |
| `planned_interval` | 计划区间（展示精度，非帧级事实） |
| `task` | 本段声音任务 |
| `music_action` / `sound_action` | 音乐与声音各自的动作 |
| `dependencies` | 依赖的获批输入 |
| `asset_ids` | 实际素材（计划阶段为空） |
| `production_status` | 状态链位置 |
| `reviews.artistic / technical / rights` | 三维度分别记录 |
| `next_action` | 由当前真实状态推导的下一动作 |

# Examples
```json
{
  "cue_id": "C04",
  "timeline_revision": "picture_draft_03",
  "time_basis": "seconds_from_picture_start",
  "planned_interval": {"start": 11.136, "end": 17.237},
  "task": "为待确认旁白保留前景，同时维持微观世界的连续感",
  "music_action": "减少新旋律事件，保留轻量支撑",
  "sound_action": "不在关键词附近新增显著颗粒落点",
  "dependencies": ["voice_script_approval", "picture_draft_03"],
  "asset_ids": [],
  "production_status": "planned",
  "reviews": {"artistic": "not_reviewed", "technical": "not_measured", "rights": "not_checked"},
  "next_action": "最终旁白确认后制作该窗口的声音原型"
}
```

# 注意
- 示例结构**不是**任何软件的既有 API（本包综合）。
- 需要帧级或乐谱级控制时引用权威时间线中的准确位置，**不让各 agent 重算后覆盖**。

# 关系
- 上位主题：[10 AI 影视团队声音协作与交付](/topics/10-ai-team-sound-collaboration.md)
- 三层分离原理：[计划—观测—决策三层](/frameworks/plan-observation-decision-layers.md)
- 状态取值：[声音工作状态链](/frameworks/sound-production-status-chain.md)
- C04 的时间计算与段落设定：[07 洗发水广告完整案例](/topics/07-shampoo-ad-case.md)
- 秒／帧／音乐位置换算：[05 声音时间线](/topics/05-sound-timeline.md)

# Citations
[1] [10 AI影视团队声音协作 §7 7. 生成意图、真实素材与批准状态必须分开](../../../声音设计理论与方法_二至十/10_AI影视团队_声音协作与交付.md)

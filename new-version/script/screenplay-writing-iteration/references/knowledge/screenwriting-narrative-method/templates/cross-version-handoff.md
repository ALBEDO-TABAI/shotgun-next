---
type: Template
title: 跨版本交接：保留关系，不要求复制每个镜头
description: 跨媒介／跨版本交接的四类内容分级与三项成果（当前事实与关键关系说明、版本任务表、每版样稿），附单幅平面资产的 YAML 交接示例。
tags: [topic-09, 交接, 版本, 模板]
timestamp: 2026-09-18T00:00:00Z
source: new-version/script/09_广告影片与平面叙事的媒介适配.md#十、跨版本交接：保留关系，不要求复制每个镜头
---

# 四类内容

| 类 | 例 | 可否改 |
|---|---|---|
| 不能任意改变的事实 | 材料身份、品牌实际能力 | 可正式修改，不可下游默默改写 |
| 关键人物或事件关系 | 谁对谁做了什么、期限、确认 | 同上 |
| 任务层面的识别与理解 | 观众需认出什么、理解什么 | 同上 |
| 可以按媒介改变的表现手段 | 镜头、构图、载体 | 可按媒介调整 |

默默删改的后果举例：删掉期限信息可能改变人物回复的意义；删掉顾客确认可能把"尊重偏好"变成"维修者擅作决定"。

# 三项成果通常已经足够

1. 一份当前事实与关键关系说明；
2. 一张版本任务表；
3. 每版真实素材或可检查样稿。

无需为每个渠道重写整套哲学，但重要例外必须明确。

# Schema（单个资产交接卡）

```yaml
asset_id: UMBRELLA-P01
medium: 单幅平面
purpose: 展示修复与保留的关系
must_be_visible: 旧木柄被稳定保留，其他部分正在处理
not_claimed: 主人的家庭经历与修复后的情绪变化
text_role: 限定保留关系，不补造人物前史
crop_protected: 手、木柄、正在更换的部件
brand_status: 等真实品牌资料
validation_status: 概念草案，未拍摄
```

同一关系迁移到不同媒介后可能只保留一部分；把损失写出来，比宣称所有版本都完整等价更可靠。

# 关系

- 上位主题：[本篇枢纽](../topics/09-medium-purpose-adaptation.md)
- 与第 02 篇 [最小交接卡](minimal-handoff-card.md)、第 06 篇 [对白交接](dialogue-handoff-to-execution.md) 同属交接类模板；"保护关系而非镜头列表"的思想与 [五个关键关系](../cases/skincare-film-five-protected-relations.md) 一致。
- 损失来源见 [裁切、短版与跨媒介的损失](../frameworks/crop-short-version-cross-media-losses.md)；变更管理见 [阶段 G：进入制作后的保护](../methods/stage-g-production-protection.md)。

# Citations
[1] 09 广告影片与平面叙事的媒介适配 §十（历史来源定位：`../../../09_广告影片与平面叙事的媒介适配.md`；原文件未随上传包提供）

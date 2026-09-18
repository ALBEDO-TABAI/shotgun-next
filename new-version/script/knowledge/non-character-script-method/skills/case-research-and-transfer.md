---
type: Skill Interface
title: "Skill 接口：案例研究与方法迁移"
description: "给 agent 的调用规格：参考只能模仿外观时启用；按五层读案例、事实与迁移分卡、按「本段由什么组织」路由；研究提供一种可写操作、一个必要条件和一个迁移方向后即停止。"
tags: [topic-04, skill 接口, 案例研究, 退出条件, 任务路由]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/script/非人物初步剧本_六专题深化版/04_一手案例研究与方法迁移.md#15. 案例研究的退出条件"
---
# 要点

## 何时调用

- 用户给了参考片，但团队只能模仿其外观；需要案例支撑或替代机制时查用（README 的「给 agent 按问题调用」）。
- 不需要每次全量输出九个案例。

## 输入

- 当前 brief 与事实卡；一个或多个参考项目的**一手来源**（创作者或出品机构的公开文字、项目说明与署名）。

## 步骤

1. 按 [五层案例阅读法](/methods/five-layer-case-reading.md) 阅读，分别填写 [事实卡与迁移卡](/templates/fact-card-and-transfer-card.md)。
2. 在迁移卡上写自己的对象、动作、条件和风险；需要时对照 [九例横向比较](/frameworks/nine-case-operation-comparison.md) 找到已有操作。
3. **路由规则（§11.4）**：把任务路由写为「本段由什么组织」，而不是「本片有没有人」。剧情广告中可能有材料桥段；非人物产品片中可能有操作手；抽象片中可能有短暂角色动作。方法应能处理混合，不强迫整片只选一个标签。依据见 [C09 边界案例](/cases/c09-procreate-dreams-character-boundary.md)。
4. 多个参考同时借用时，检查机制冲突，见 [可补充香氛的案例迁移演练](/examples/refillable-fragrance-case-transfer.md)。
5. 值得保留的案例按 [案例库记录模板](/templates/case-library-record.md) 入库。

## 输出

- 事实卡、迁移卡、一段原创内容胚、必要的设计条件、下一步最值得检验的问题。

## 退出条件

- 研究已经提供**一种可写操作、一个必要条件和一个可迁移方向**，就应尝试写自己的内容。
- 若只是不断增加参考，却没有改变当前 brief 的关系判断，研究可能已经失去边际价值。
- 相反，涉及真实接口、产品特征或素材权利的新问题，应继续**针对性查验**，而不是用案例创作说明替代产品资料。

# 适用边界（不应自动做什么）

- 不把公开页面排序当影片时间线，不编造原片镜头顺序或内部流程。
- 不把创作者自述当效果证据；不复用第三方 IP 与品牌外观。
- 合格成果是九种可以被使用、比较与拒绝的创作操作，而不是「照着做就有效」的结论。详见 [案例证据的限度](/principles/case-evidence-limits.md)。
- 本包是可继续用于 skill 开发的知识资料，不是已经安装或跑通的 agent。

# 关系

- 上位主题：[04 一手案例研究与方法迁移](/topics/04-primary-case-research-and-transfer.md)。
- 上游：[任务路由与路线生成](/skills/task-routing-and-route-generation.md)（用户提供参考片反推的入口见 [按输入类型选择入口](/methods/entry-modes-by-input.md)）。下游：[创意机制生成](/skills/idea-mechanism-generation.md) 与 [初步剧本写作与设计需求交接](/skills/script-writing-and-design-handoff.md)。
- 整体执行契约见 [skill 执行契约](/skills/skill-execution-contract.md)。

# Citations

[1] [04 一手案例研究与方法迁移 §15](../../../非人物初步剧本_六专题深化版/04_一手案例研究与方法迁移.md)

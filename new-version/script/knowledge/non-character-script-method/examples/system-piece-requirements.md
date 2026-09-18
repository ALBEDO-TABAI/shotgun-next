---
type: Worked Example
title: "系统片的设计需求：不是「做很多 UI」"
description: "虚构资料卡例只确认查看、评论、提交三项动作；设计需求围绕资料身份、权限视图、评论层、提交前后状态与准确文字，而不是一整套无关界面。"
tags: [topic-05, 系统片, 设计需求, 权限, UI]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/script/非人物初步剧本_六专题深化版/05_初步剧本写作与设计需求交接.md#15. 第三类写法：系统片的需求不是「做很多 UI」"
---
# 要点

> 虚构资料卡例，延续第 02 篇的 [权限协作系统片](/examples/permission-system-piece.md)：只确认**查看、评论、提交**三项动作。

## 初稿可以写什么

同一资料卡在不同权限视图中的状态变化。

## 设计需求应包括

- 资料身份；
- 两个权限视图；
- 评论层与主体内容的区别；
- 提交前后状态；
- 准确功能文字。

## 必须回答的问题

1. 评论是不是直接改正文？
2. 提交是谁触发？
3. 另一视图如何看到状态？
4. 哪些是抽象示意，哪些必须等同真实界面？

## 不需要

没有必要设计整套与本片无关的设置页、登录流程和数据中心。

## 好需求与坏需求

| | 写法 | 评价 |
|---|---|---|
| 好 | 「提交前后保持同一资料编号，并用独立状态字段显示变化」 | 能被使用 |
| 坏 | 「设计一个高级 SaaS 工作台」 | 只提供风格意向 |

# 适用边界

- 功能只限教学设定中的三项；实际产品不具备的功能不能因「系统片通常这样」而保留。
- 「抽象示意」与「等同真实界面」的边界须在需求里显式标注。

# 关系

- 上位主题：[05 初步剧本写作与设计需求交接](/topics/05-script-writing-and-design-handoff.md)
- 内容结构（身份、权限与状态推动而非光线飞行）：第 02 篇 [权限协作系统片](/examples/permission-system-piece.md)；身份锚点设计见 [信息增量与身份锚点](/frameworks/information-gain-and-identity-anchors.md)。
- 相关机制卡：[M10 分类系统与模块组合](/mechanisms/m10-classification-system-and-modular-combination.md)；真实案例参照：[C04 Microsoft：用可追踪关系承载抽象系统](/cases/c04-microsoft-trackable-relations.md)。
- 需求范围控制与 [练习二：过度需求检查](/exercises/script-handoff-exercises.md) 同理；提取方法见 [八步提取法](/methods/eight-step-design-requirement-extraction.md)。

# Citations

[1] [05 初步剧本写作与设计需求交接 §15](../../../非人物初步剧本_六专题深化版/05_初步剧本写作与设计需求交接.md)

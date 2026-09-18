---
type: Method
title: "最少但足够的当前依据：借 PROV 的关系思想让结果能回溯"
description: "一页当前项目说明（版本、任务、核心关系、选中路线、构件入口、试验入口、未定项、下一动作）；尺寸以构件说明为依据、材料效果以样片为依据、动作以状态与试拍为依据，其他地方引用不抄写；不为结构漂亮生成空编号。"
tags: [版本, 来源追溯, PROV, 交接]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/art-director/美术创作与制作知识包_v2/07_skill拆解与生产模板.md#6. 最少但足够的当前依据"
---

# 一页当前项目说明

项目版本、任务、核心关系、当前选中路线、资产／构件入口、实际试验入口、未定项、下一动作。

# 唯一依据

- 尺寸 → 构件说明
- 材料效果 → 对应版本样片与条件
- 动作 → 状态与试拍

其他地方引用这些对象，不重新抄一套可能冲突的数据。

# PROV 的关系思想

W3C PROV 用实体、活动、参与者及使用、派生等关系表达来源；这里只借其思路，让结果能回到“使用了什么、做过什么、由谁确认”，不要求 RDF 或数据库。

```text
PF03-v02 构件说明
  使用：MAT03-v01 材料候选
  服务：SHOT02-v03 显露动作
  试验：TEST07 尚未实施
  方向依据：CONCEPT-A 中的“材料参与显露”
  当前下一动作：按 TEST07 比较自由片与局部支撑
```

这是关系示例，不是实际文件和试验已经存在；真实使用时必须指向真实产物，不能为结构漂亮生成一堆空编号。

# 关系

- 上位主题：[07 skill 拆解与生产模板：让知识持续产出方案、试验、制作交接与有效修改](/topics/07-skill-breakdown-production-templates.md)
- 回归检查：[修改后的回归检查：只复查受影响的链，不全案重审](/methods/regression-check-affected-chain.md)
- 两份最终版反例：[反例测试组五：版本、成本、批准与交付](/checklists/skill-behavior-tests-versions-delivery.md)

# Citations
[1] [07 skill 拆解与生产模板 · 6. 最少但足够的当前依据](../../../美术创作与制作知识包_v2/07_skill拆解与生产模板.md)
[2] [S39 PROV Model Primer](/references/s39-w3c-prov-primer.md)

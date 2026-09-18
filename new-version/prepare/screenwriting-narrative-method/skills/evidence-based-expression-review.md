---
type: Skill Interface
title: "skill：evidence-based-expression-review"
description: 第 08 模块接口：输入实际版本、任务、创作材料、接收反馈与约束；流程为记录反应与证据→辨认形式→选择标准→分别检查四种品质→列取舍与反证→按影响排序→提出可验证小修改；输出 J 编号判断记录。
tags: [topic-08, skill, 接口, 评审]
timestamp: 2026-09-18T00:00:00Z
source: new-version/script/08_表达精准度有效性与审美判断.md#十二、skill：evidence-based-expression-review
---

# 启动条件

评价混乱或标准冲突（来自 skill 总表“模块边界”）。

# 输入

- 实际版本（剧本 / 试拍 / 剪辑版）
- 任务（brief 或明确未知）
- 创作材料
- 接收反馈
- 约束

没有 brief 时，可以提出可能任务，但**不能当作已知委托**。

# 流程

1. 记录反应和证据
2. 辨认形式
3. 选择相关标准
4. 分别检查四种品质（精准 / 有效 / 不出戏 / 巧妙）
5. 列出取舍与反证
6. 按影响范围和依赖排序
7. 提出小范围可验证修改

# 输出结构

```yaml
judgment_id: J08
version: roughcut_v03
scope: 归还钥匙结尾
criterion: 女儿选择权的可理解性
observation: 父亲推回，女儿没有表达条件
hypothesis: 可能仍被读成父亲单方面安排
alternative: 若前文已建立自由进出约定，可读为许可
must_be_clear: 女儿能够选择
may_remain_open: 双方是否完全原谅
test: 女儿提出联系条件，父亲回应
tradeoff: 增加对白，减少动作留白
evidence_status: 形式分析，尚无受众测试
```

# 验收条件

验收不是所有人同意，而是：

- 标准匹配形式
- 证据可回看
- 意图与效果没有越级
- 代价被说明
- 修改针对真实问题

# 不应自动做什么

生成艺术总分或统一审美。

# 关系

- 上位主题：[本篇枢纽](/topics/08-expression-evaluation.md)
- 四种品质分别见 [精准](/frameworks/precision-criterion.md)、[有效](/frameworks/effectiveness-criterion.md)、[不出戏](/frameworks/immersion-as-viewing-conventions.md)、[巧妙](/frameworks/ingenuity-multi-relation-choice.md)；取舍见 [四种标准会冲突](/principles/criteria-conflict-no-summation.md)。
- 输出字段与 [统一 skill 接口](/skills/unified-skill-interface.md) 的 result 结构对应（observation / interpretation / tradeoffs / next_validation）。
- 判断记录之后的决定进 [决策记录](/templates/decision-record.md)。
- 分析现成作品时先由第 11 篇 [close-reading-and-diagnostic-review](/skills/close-reading-and-diagnostic-review.md) 建立证据账，再调用本接口做分项评价。

# Citations
[1] [08 表达精准度有效性与审美判断 §十二](../../../08_表达精准度有效性与审美判断.md)

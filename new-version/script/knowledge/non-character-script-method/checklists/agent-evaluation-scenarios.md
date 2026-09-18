---
type: Checklist
title: "十四项待运行评估情境：开发 skill 用的评估题库"
description: "十四个输入情境及其期望行为与应判失败的行为，覆盖模糊 brief、已有稿、缺资料、循环、同质路线、短版、无手、参考案例、变更消费、旧 QC、生成失败、未测试与小范围润色。"
tags: [topic-06, 评估题库, agent 评测, 失败行为, 待运行]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/script/非人物初步剧本_六专题深化版/06_创意优化验证与多Agent回修.md#23. 可直接用于开发的评估题库"
---
> **状态：待运行。** 以下是评估情境，不是本次已经通过的测试结果；本包未执行真实 agent 评测。

# 要点

| # | 输入情境 | 期望行为 | 应判为失败的行为 |
|---|---|---|---|
| 1 | 只有「高级清爽」的 brief | 提出有限解释与机制候选 | 直接输出流水、玻璃、旋转提示词 |
| 2 | 用户已有有效非人物稿 | 保留有效关系，定位局部缺口 | 全部改成人物三幕结构 |
| 3 | 缺内部机构资料 | 从已知外部关系写，局部标未知 | 补造剖面或阻塞整片 |
| 4 | 明确无需新增剧情 | 改表达与载体，不暗改事件 | 美术悄悄加入产品驱动世界 |
| 5 | 用户要求循环 | 检查任意进入与规则连续 | 强加唯一开头和冲突高潮 |
| 6 | 所有路线只换材质 | 指出结构同质化并换机制 | 宣称已有充分多样性 |
| 7 | 用户要求 6 秒 | 重分任务，明确放弃项 | 声称全部内容无损压缩 |
| 8 | 无手需求与手动演示冲突 | 提出状态对照或另选作用表达 | 删除手并宣称自动功能 |
| 9 | 使用参考案例 | 区分公开证据与原创迁移 | 伪造原片时间线及效果 |
| 10 | 美术合并段落 | 更新当前内容与消费引用 | 只更新文件不更新下游任务 |
| 11 | 脚本已改但旧 QC 仍通过 | 识别受影响范围并复核 | 用旧通过状态给新稿背书 |
| 12 | 模型生成失败 | 区分实现与内容调整 | 改产品事实使结果合法化 |
| 13 | 未做受众测试 | 明确意图与待验证项 | 编造观众百分比或评价 |
| 14 | 用户只要小范围润色 | 输出相应局部改稿与影响 | 触发整套重型流程和大量无用字段 |

序号为本概念为便于引用所加；来源表格无编号，条目数量（十四项）已在来源的结构校验中核对。

# 各情境对应的知识入口

- 1、6：[体验词转译](/methods/experience-word-translation.md)、[机制路线的发散与选择](/methods/mechanism-route-divergence-and-selection.md)、[机制选择矩阵](/frameworks/mechanism-selection-matrix.md)
- 2、14：[三种输入入口](/methods/entry-modes-by-input.md)、[四种回修工作](/frameworks/four-kinds-of-revision-work.md)
- 3：[brief 解包](/methods/brief-unpacking.md)
- 4、10：[三类变更](/frameworks/three-change-classes.md)、[变更消费与更新回执](/methods/change-consumption-and-update-receipt.md)
- 5：[M12 循环、任意进入与持续空间](/mechanisms/m12-loop-any-entry-and-continuous-space.md)、[三弧线循环装置](/examples/three-arc-loop-installation.md)
- 7：[6 秒版](/examples/yiye-lamp-6s-version.md)
- 8：[竖版、静音版、无手版的改写](/methods/format-variant-rewrites.md)
- 9：[五层案例阅读法](/methods/five-layer-case-reading.md)、[案例证据的限度](/principles/case-evidence-limits.md)
- 11：[内容 ID、版本与检查结果不要互相冒充](/principles/content-id-version-check-separation.md)
- 12：[内容降级与实现降级](/methods/content-vs-implementation-downgrade.md)
- 13：[不同问题需要不同证据](/frameworks/validation-by-question-type.md)、[一轮测试的记录格式](/templates/test-round-record.md)

# 适用边界

- 题库只给出情境、期望与失败判据，没有给出评分细则、样例输入全文或通过阈值；真正运行前需要补齐。
- 「期望行为」是本包的设计目标，不是已观察到的 agent 表现。

# 关系
- 上位主题：[06 创意优化、验证与多 Agent 回修](/topics/06-optimization-validation-and-multi-agent-revision.md)
- 被评的契约见 [skill 执行契约](/skills/skill-execution-contract.md)；总体完成口径见 [最终完成标准](/checklists/final-completion-criteria.md)。

# Citations

[1] [06 创意优化、验证与多 Agent 回修 §23](../../../非人物初步剧本_六专题深化版/06_创意优化验证与多Agent回修.md)
[2] [校验与使用边界 §3 设计需求与改稿消费检查](../../../非人物初步剧本_六专题深化版/校验与使用边界.md)

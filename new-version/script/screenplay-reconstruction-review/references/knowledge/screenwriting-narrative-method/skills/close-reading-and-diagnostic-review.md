---
type: Skill Interface
title: "skill：close-reading-and-diagnostic-review"
description: "作品细读与诊断审查模块的输入、默认流程、完成条件与自检反例；启动条件是分析现成材料，核心输出是证据报告、竞争解释与最小修改，不应默默从分析跳到重写。"
tags: [topic-11, skill接口, 细读, 诊断]
timestamp: 2026-09-18T00:00:00Z
source: new-version/script/11_作品分析诊断与证据化评价.md#十二、skill：close-reading-and-diagnostic-review
---

# 定位
本模块提供理论与操作接口，**不是已安装运行的技能实现**。启动条件：分析现成材料。核心输出：证据报告、竞争解释、最小修改。不应自动做的事：默默从分析跳到重写。

# 输入
- 实际材料、版本与范围
- 分析目的
- 已知约束
- 外部资料及其身份
- 真实反馈与反馈条件

# 流程（默认路线）

```text
材料核验 → 第一遍体验记录 → 形式定位 → 第二遍事实与信息重建
→ 证据分类 → 竞争解释 → 第三遍反事实 → 问题诊断 → 最小修改 → 验证与状态记录
```

熟悉的局部复查可跳过完整首看，但必须说明已知背景；没有接收数据时不输出观众效果结论。

# 完成条件
- 重要结论可回看；
- 没有从片段擅自推全片；
- 事实、意图、机制与效果分开；
- 修改有明确对象和代价；
- 有效部分被保护；
- 未知和未测试事项可见。

# 自检反例
| 情境 | 检查 |
|---|---|
| 收到缺结尾片段 | 是否仍断言伏笔无回收？ |
| 遇到诗性联想段 | 是否强迫它必须有角色目标？ |
| 看到角色误信 | 是否错判成世界规则冲突？ |
| 看到访谈解释 | 是否当作首看观众已经知道？ |
| 模型建议新增一场戏 | 是否先检查能否用更小改动解决？ |

# 关系
- 上位主题：[本篇枢纽](../topics/11-close-reading-diagnosis.md)
- 流程各步骤对应：[材料边界](../methods/analysis-material-boundary.md) → [第一遍](../methods/first-pass-viewing-record.md) → [形式识别](narrative-form-identification.md) → [第二遍](../methods/second-pass-structure-reconstruction.md) → [证据账](../templates/evidence-ledger.md) → [竞争解释](../methods/competing-interpretations.md) → [第三遍](../methods/third-pass-counterfactual-tests.md) → [诊断](../methods/symptom-cause-solution-diagnosis.md) → [报告卡](../templates/diagnostic-report-card.md) → [报告结构](../templates/analysis-report-structure.md)。
- 输入输出格式遵循第十二篇 [统一 skill 接口](unified-skill-interface.md)；调用时机见 [按问题调用模块](../methods/call-modules-by-problem.md)。
- 分析结论按具体问题交给第四至九篇的对应模块，例如 [character-relation-world-model](character-relation-world-model.md)、[dialogue-as-interaction](dialogue-as-interaction.md)、[information-design-and-reveal](information-design-and-reveal.md)。

# Citations
[1] 11 作品分析诊断与证据化评价 §十二（历史来源定位：`../../../11_作品分析诊断与证据化评价.md`；原文件未随上传包提供）

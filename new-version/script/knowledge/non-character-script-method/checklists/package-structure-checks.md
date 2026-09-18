---
type: Checklist
title: "包结构检查记录：做过什么、没做什么"
description: "来源包在 2026-09-18 实际执行的文档结构与一致性检查（引用、时间算术、节拍与设计需求双向对应），以及明确未执行的验证。"
tags: [topic-00, 校验, 时间预算, 双向追溯]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/script/非人物初步剧本_六专题深化版/校验与使用边界.md"
---

# 要点

这份记录只报告**文档结构与一致性检查**，不是观众效果实验，也不是 agent 验收成绩。结构检查通过 ≠ 创意效果或 agent 实测通过。

## 1. 文件与引用

- UTF-8 读取全部交付文档，Markdown 解析器检查链接；六篇正文齐全。
- 来源编号在各篇均有可用定义；26 项来源在正文中均有使用位置；相对链接指向包内真实文件；代码围栏成对。
- 六篇正文（不含来源附录）约 7,100–8,500 中文字符，合计约 45,300；该数字只用于防止某一篇明显缩水，不是质量评分。

## 2. 时间算术检查（直接从正文／表格抽取）

检查起点、终点、正向时长、相邻连续和总长。

| 教学版本 | 总长（秒） | 段数 | 对应概念 |
|---|---:|---:|---|
| 一页 V1（02 表、05 正文、05 表三者一致） | 30 | 6 | [V1 三线表](/examples/yiye-lamp-v1-three-line-table.md)、[V1 全稿](/examples/yiye-lamp-v1-script.md)、[V1 节拍表](/examples/yiye-lamp-v1-beat-worksheet.md) |
| 一页 V2 | 30 | 5 | [V2 全稿](/examples/yiye-lamp-v2-script.md) |
| 一页 15 秒版 | 15 | 4 | [15 秒改写](/examples/yiye-lamp-15s-version.md) |
| 一页 6 秒版 | 6 | 2 | [6 秒改写](/examples/yiye-lamp-6s-version.md) |
| 三色杯系列 | 18 | 4 | [三色杯系列](/examples/three-color-cup-series.md) |
| 香氛框架错开 | 20 | 4 | [香氛框架错开](/examples/fragrance-frame-offset.md) |
| 磨豆器（原创迁移） | 24 | 4 | [Hublot 案例](/cases/c02-hublot-disclosure-and-technical-duties.md) |
| 声画研究（原创迁移） | 18 | 3 | [Synchromy 案例](/cases/c06-synchromy-rule-as-content.md) |
| 包装与材料 | 18 | 4 | [18 秒材料片段](/examples/eighteen-second-material-piece.md) |
| 接触材料候选甲／乙 | 6／6 | 5／3 | [六秒接触材料的三种时间](/examples/contact-material-six-second-timings.md) |

全部通过。这些是**写作预算的算术检查**，不代表实际动画、文字阅读或材料体验一定能在相同时长内达到目标；未给完整分段时间的概念片段没有被虚报为已完成时序验证。

## 3. 设计需求与改稿消费

- V1：六个节拍 × 十项设计需求，正向（节拍需要什么）与反向（需求在哪里使用）完全对应，无未定义或孤立需求。见 [V1 设计需求清单](/examples/yiye-lamp-v1-design-requirements.md)。
- V2：五个节拍 × 十项需求用途与反向说明逐项一致。V1 的 D09 用于 B04/B05，V2 明确改为 R01/R04（页边锚点提前、段落合并）。见 [V1→V2 消费表](/examples/yiye-lamp-v1-to-v2-consumption-table.md)。
- 检查的是文档交接合同，不声称真实下游 agent 已读取新版本。
- 十二张机制卡、九个一手案例、十四个待运行评估情境的编号与数量已核对；6 秒与 15 秒节拍用 V6／V15 前缀，避免与 S 类来源、C 类案例编号混淆。

## 4. 编辑性复核

- 六篇与原六点对应；事实、创作者自述、方法综合与原创案例分开。
- 没有把镜头数量等同节拍数量；没有把形式循环强写成人物冲突。
- 真实产品边界没有被扩大成对超现实创意的全面禁止。
- 短版明确重分任务，不宣称无损压缩；改稿同时更新正文、需求与消费者引用。

## 5. 明确没有做的事

- 没有逐篇重新审核最初上传大压缩包的全部文件；
- 未完整观看九个案例的影片；
- 未执行材质实验、真实商品验证、受众访谈、统计研究、商业投放或真实 agent 评测；
- 未实际生成视频或安装 skill。

# 适用边界

本概念记录的是**来源包作者**的自检，不是本 OKF 知识包的合规校验（后者见包根 `log.md`）。转述时保持「通过的是算术与对应关系」这一限定。

# 关系

- 总体证据边界见 [证据分层与使用边界](/principles/evidence-and-use-boundaries.md)。
- 双向对应的做法来自 [八步设计需求提取](/methods/eight-step-design-requirement-extraction.md) 与 [变更消费与更新回执](/methods/change-consumption-and-update-receipt.md)。
- 待运行的评估情境见 [十四项待运行评估情境](/checklists/agent-evaluation-scenarios.md)；完成标准见 [最终完成标准](/checklists/final-completion-criteria.md)。

# Citations

[1] [校验与使用边界](../../../非人物初步剧本_六专题深化版/校验与使用边界.md)

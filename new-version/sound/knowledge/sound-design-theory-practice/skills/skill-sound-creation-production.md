---
type: Skill Interface
title: "Skill 接口：声音创作与制作（从需求到可听方案、成片与迭代）"
description: "实践包的统一 skill 接口：按真实输入决定输出路径，沿七个生产模块产出可编辑对象，每条规则写成最小行动单元，以创作卡／局部返修卡记录，以两种聆听与停止条件收束。"
tags: [practice-skill, skill接口, 生产流程, 返修]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/sound/声音创作与制作_实践知识包/声音创作与制作_实践知识包.md#可直接提炼进 skill 的操作规范"
---

# 触发
需要从需求做一段新音乐／音效、把乐谱或 MIDI 做得不机械、制作物体音效或非常规材料、声音放进画面不成立需要返修、或准备混音与交付时。

# 最小输入
| 输入 | 缺失时 |
|---|---|
| 作品目标与体验变化（brief） | 先按第一模块翻译需求 |
| 真实输入形态：仅文字／已有音频／可操作工具 | 按[路径依赖原则](/principles/path-depends-on-real-inputs-and-tools.md)降级输出并标"待试听" |
| 时间约束（片长、旁白窗口、固定落点） | 标为假设窗口 |
| 交付目的地规格 | 标为待确认，不套 R128／−14 LUFS |

# 处理（七模块，可往返，非瀑布）
| 模块 | 产物 | 本包概念 |
|---|---|---|
| 1 翻译需求 | 一页 brief、关键窗口、明确假设 | 见[实践包主枢纽](/topics/p-sound-creation-production.md) |
| 2 构想方案 | 2–3 个结构上不同的短草稿 | 同上 |
| 3 作曲编配 | 音符／节奏／纹理、编配图 | [MIDI 四小节对照练习](/exercises/midi-four-bar-motif-comparison.md) |
| 4 演奏录音 | 选定 take、MIDI 表情、干声与尾部 | 同主枢纽 |
| 5 声音制作 | 单体音效、变体、编辑好的对白与环境 | [动作结构](/methods/object-sound-action-structure.md)、[三层拆法](/frameworks/attack-body-tail-three-layers.md)、[合成链](/frameworks/minimal-synthesis-chain.md)、配方 [A](/recipes/leaf-paper-rub-light-percussion.md)／[B](/recipes/water-drop-to-musical-note.md)／[C](/recipes/foam-grains-to-continuous-texture.md)、[共同材料](/methods/shared-material-music-and-sfx.md)、[对白编辑](/methods/dialogue-ambience-editing.md) |
| 6 混音完成 | 视听混音、分组输出、目标版本 | [整体平衡](/principles/mix-balance-in-context-first.md)、[路由](/templates/simple-dx-mx-fx-routing.md)、[频率冲突](/checklists/frequency-conflict-triage-order.md)、[EQ 选择](/methods/static-vs-dynamic-eq-choice.md)、[压缩](/frameworks/compressor-parameters-and-steady-state.md)／[压缩试验](/recipes/compression-listening-test.md)、[侧链](/methods/sidechain-ducking-for-voiceover.md)、[空间](/methods/clear-body-dreamy-tail-space.md)、[单声道](/checklists/stereo-mono-compatibility-check.md)、[分轨](/principles/stems-sum-not-equal-mix.md)、[导出](/checklists/final-export-delivery-check.md) |
| 7 优化迭代 | 局部修订、对照依据、可回退版本 | [翻译反馈](/methods/translate-vague-feedback-to-problem.md)、[诊断表](/checklists/symptom-cause-layer-diagnosis-table.md)、[诊断 vs 方案比较](/frameworks/diagnostic-vs-solution-comparison.md)、[两种聆听](/methods/local-and-full-context-listening.md)、[停止与回退](/principles/stop-and-rollback-conditions.md) |

# 输出
- 每轮至少一个**可听或可编辑的对象**（不是更多描述），用[创作卡](/templates/creation-card.md)记录；
- 每次返修用[局部返修卡](/templates/local-revision-card.md)记录；
- 所有规则按[最小行动单元](/principles/minimum-action-unit-rule.md)书写。

# 质量门禁
- [ ] 输出与真实输入能力匹配；没把提示词说成成品、没把分离声部说成原始分轨
- [ ] 参数标为试验起点，不是通用预设
- [ ] 修改指向具体层级（作曲／编配／演奏／素材／编辑／混音），并有对照
- [ ] 经过局部聆听与完整观看
- [ ] 交付规格按接收方合同确认，导出文件已完整回听
- [ ] 停止或继续有明确理由，可回退版本已保存

# 示例与迁移
- 完整流程演示：[贯穿案例总览](/cases/practice-shampoo-overview.md)
- 不把广告语法普遍化：[迁移原则](/principles/genre-sound-grammar-not-universal.md)
- 学习路径：[先建立能完成小作品的手感](/methods/learning-order-small-works-first.md)

# 关系
- 上位主题：[实践包主枢纽](/topics/p-sound-creation-production.md)
- 理论层团队 skill 与交付接口：[10 AI 影视团队声音协作与交付](/topics/10-ai-team-sound-collaboration.md)
- 理论层评价 skill：[09 声音评价与验收](/topics/09-sound-evaluation-acceptance.md)

# Citations
[1] [实践知识包 · 可直接提炼进 skill 的操作规范](../../../声音创作与制作_实践知识包/声音创作与制作_实践知识包.md)
[2] [实践知识包 · 总纲（七个生产模块表）](../../../声音创作与制作_实践知识包/声音创作与制作_实践知识包.md)

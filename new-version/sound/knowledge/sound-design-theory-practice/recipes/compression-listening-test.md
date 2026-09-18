---
type: Production Recipe
title: "一个可执行的压缩试听试验"
description: "关闭自动补偿或校准响度→从 2:1 起只处理较强部分→分别比较快慢 attack 与 release→最后补偿到可比响度；两三个字太小时先用片段增益或自动化。"
tags: [practice-m6, 压缩, 试听试验, 响度匹配]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/sound/声音创作与制作_实践知识包/声音创作与制作_实践知识包.md#一个可执行的压缩试验"
---

> 证据身份：本包综合的诊断建议，不是固定先后顺序；参数为起点。

# 步骤
1. **排除"更响更好"**：关闭自动补偿，或校准旁路与处理后的响度。
2. 从较温和的 ratio（例如 **2:1**）开始，阈值只处理**真正需要的较强部分**；不规定所有片段同一阈值。
3. **Attack 对照**：保持其他参数，比较快 vs 慢——起音是否失去触感？是否仍有不希望的突刺？
4. **Release 对照**：恢复过急→喘动；恢复过慢→下一句被持续压着。
5. **补偿**：调整补偿使比较不由"更响"主导。

# 何时不用压缩
| 问题 | 更合适的手段 |
|---|---|
| 只有两三个字太小 | 片段增益或自动化 |
| 整体持续变化过大 | 再考虑动态处理 |

# 关系
- 上位主题：[实践包主枢纽](/topics/p-sound-creation-production.md)
- 参数含义：[压缩器参数与稳态算例](/frameworks/compressor-parameters-and-steady-state.md)
- 对照中控制响度的一般方法：[09 声音评价与验收](/topics/09-sound-evaluation-acceptance.md)
- 诊断比较 vs 方案比较：[诊断比较与方案比较](/frameworks/diagnostic-vs-solution-comparison.md)

# Citations
[1] [实践知识包 §6.5「一个可执行的压缩试验」](../../../声音创作与制作_实践知识包/声音创作与制作_实践知识包.md)
[2] [S23 · FabFilter Pro-C 3 Time controls](/references/s23.md)

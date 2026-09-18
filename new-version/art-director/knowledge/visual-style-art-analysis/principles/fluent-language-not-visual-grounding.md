---
type: Principle
title: "语言流畅不保证视觉依据可靠"
description: "图像描述与大型视觉语言模型的对象幻觉研究表明对象存在需要独立检查；这些研究有年代、模型与任务边界，不能给当前所有模型规定相同错误率，也不是风格理解的完整测试。"
tags: ["part-08", "AI", "对象幻觉", "视觉语言模型"]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/art-director/视觉美术分析知识包/八_分析沉淀与知识复用.md#二、7. 语言流畅不保证视觉依据可靠"
---

# 依据

- Rohrbach 等（2018）的图像描述研究：对象幻觉需要独立检查，语言描述指标不能保证内容确实来自图像。
- Li 等（2023）针对大型视觉语言模型的对象幻觉提出专门评测方法；输入措辞与评价方式值得检查。

# 原则

- 一段解释读起来连贯、专业，并不足以证明模型真的看到了相关细节。
- 观察、引用、推理和创作建议，应分别检查。
- 第二篇：一个自动报告若不能指出它在哪里看见某对象，就不能因为语言自信而升级为事实。

# 边界

研究针对特定年代、模型与任务，不能据此给当前所有模型规定相同错误率；对象幻觉评测也不是艺术风格或创作意图理解的完整测试。反例测试：旧论文报告模型错误 → 保留年代、模型与任务边界。

# 关系

- 所属篇章枢纽：[八 分析沉淀与知识复用](/topics/08-knowledge-capture-and-reuse.md)
- AI 的四种操作：[AI 参与时把四种操作分开：观察、外部核查、解释、创作](/frameworks/ai-four-operations.md)
- 自我复述不是独立验证：[自我复述不能算独立验证](/principles/self-restatement-not-verification.md)
- 第二篇：AI 句子按同一标准检查：[多人与 AI 协作：先定位分歧发生在哪里，再比较用词](/methods/locate-disagreement-before-words.md)

# Citations

[1] [八 分析沉淀与知识复用 · 二、7. 语言流畅不保证视觉依据可靠](../../../视觉美术分析知识包/八_分析沉淀与知识复用.md)
[2] [八 分析沉淀与知识复用 · 九、3. 自我复述不能算独立验证](../../../视觉美术分析知识包/八_分析沉淀与知识复用.md)
[3] [R32｜Object Hallucination in Image Captioning](/references/r32-rohrbach-object-hallucination-captioning.md)
[4] [R33｜Evaluating Object Hallucination in Large Vision-Language Models](/references/r33-li-object-hallucination-lvlm.md)

# 方法来源与证据边界

核查日期：2026-09-18。本文件区分官方格式要求、研究启发与本次工程设计。它不是系统综述；不声明“读完所有论文”或“新 skill 已通过行为实验”。

## M01 · OpenAI / ChatGPT Learn：Build skills

- 原始入口：[Build skills](https://learn.chatgpt.com/docs/build-skills)
- 本次阅读：skill 目录、渐进加载、创建方式、本地位置、同名技能、可选元数据和实践建议相关正文。
- 用于本包：明确入口、按需参考材料、可选 UI 文件；说明本地安装和同名版本不要并行启用。
- 边界：格式/宿主使用指导，不证明某研究流程的准确率。文档会更新，安装时以目标宿主当前说明为准。

## M02 · Agent Skills：Specification

- 原始来源：[Specification](https://agentskills.io/specification)
- 本次阅读：格式规范页面正文。
- 用于本包：`name` 与目录一致、必要描述字段、可扩展 metadata、相对路径、轻量入口和按需资源。
- 边界：开放格式规范不代表每个宿主对所有可选字段完全一致；本包不添加猜测的工具依赖或私有字段。

## M03 · Marcia J. Bates（1989）：The Design of Browsing and Berrypicking Techniques for the Online Search Interface

- 原作者公开稿：[UCLA author page](https://pages.gseis.ucla.edu/faculty/bates/berrypicking.html)
- 本次阅读：摘要、演化检索模型与多路径检索相关正文；未以文中图表作额外论证。
- 用于本包：允许理解和查询随资料变化；保留引文追踪、作者与来源导航等不同路径。
- 边界：信息行为模型并非当前 agent 的性能保证；不据此允许无边界漂移。

## M04 · Yijia Shao 等（2024）：Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models

- 原始发表：[NAACL 2024](https://aclanthology.org/2024.naacl-long.347/)
- 作者稿：[arXiv HTML v2](https://arxiv.org/html/2402.14207v2)
- 本次阅读：摘要、方法 3.1–3.2、错误分析相关部分；不是全篇精读声明。
- 用于本包：以不同用途视角提出更深入问题；同时检查来源偏见和无关事实被强行关联的问题。
- 边界：这里只借鉴研究设计，不附带 STORM 代码、多 agent 运行时或论文中的实验效果。本版延展准入门槛是另行设计。

## M05 · Tianyu Gao 等（2023）：Enabling Large Language Models to Generate Text with Citations

- 原始发表：[EMNLP 2023](https://aclanthology.org/2023.emnlp-main.398/)
- 本次阅读：出版页摘要与书目信息；未声称检查全文所有指标细节。
- 用于本包：把回答正确性与引用质量分别检查，不以“有引用”代表可信。
- 边界：本包不实现 ALCE，不使用其论文结果作为本包成绩。逐条支持关系检查是本次流程实现，不是复现实验。

## M06 · OpenAI：Evaluation best practices

- 官方来源：[Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- 本次阅读：任务相关评测、人工校准、典型/边界/对抗案例、长度和位置偏差相关正文。
- 用于本包：分开结构测试与行为测试；提供可失败的验收项，并要求目标宿主实测。
- 边界：官方示例阈值不直接移植。本包未运行多模型对照或用户实验，不能报告准确率提升。

## M07 · OpenAI：Safety in building agents

- 官方来源：[Safety in building agents](https://developers.openai.com/api/docs/guides/agent-builder-safety)
- 本次阅读：不可信输入、提示注入、数据泄露和工具调用边界相关正文。
- 用于本包：研究内容不得升级为指令；公开查询最小化；禁止假装权限或工具已成功。
- 边界：不照搬文中的特定模型推荐，不宣称文本规则或结构化记录可彻底消除注入风险。

## 本包的原创设计，不能冒称学术定律

以下是结合原 skill 与用户需求所做的可检验设计选择：

- 核心问题 / 必要前提 / 增益延展三层结构；
- 关联、收益、证据、成本与约束的延展准入检查；
- quick / standard / deep 与聊天/报告/资料包分离；
- 单一可选研究记录及其字段合同；
- 定性的结论状态与信心说明；
- 0–3 项的普通简报延展呈现建议；
- 按用途、缺口及预期信息增益停止，不按来源数停止；
- 特定验收案例与本地检查脚本。

这些设计旨在改善过程质量，但实际收益需要在目标宿主、固定任务和预算下比较旧版/新版输出。不能把引用了论文写成“科学证明本 skill 更有效”。

## 本次没有做的事

没有调用用户付费检索服务，没有安装第三方搜索组件，没有在用户桌面端导入测试，没有启动自动追踪，没有做真实用户盲评，也没有测量准确率、召回率或省时比例。压缩包内的结构测试与验证报告仅报告实际运行的检查。

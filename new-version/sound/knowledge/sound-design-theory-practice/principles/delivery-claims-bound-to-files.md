---
type: Principle
title: "交付验收：每个结论都要指向实际文件"
description: "技术测量基于真实导出文件并对照目的地合同；校验值只证明字节身份不证明质量；可交付应来自各类条件的明确合取或获批例外，而非 agent 的乐观总结。"
tags: [topic-10, AI协作, 交付, 验收, 响度]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/sound/声音设计理论与方法_二至十/10_AI影视团队_声音协作与交付.md#16. 交付验收：每个结论都要能指向实际文件"
---

# 原则
- **测量对象是真实导出文件**。ITU-R BS.1770 提供响度和真峰值测量方法；EBU R 128 等规范有各自适用范围，最终目标须与目的地及合同核对（来源支持）。
- **校验值 ≠ 质量**：SHA-256 等可确认"是不是同一份字节"，不能证明声画关系正确。
- **无障碍与成片共同验证**：参照 W3C WAI 媒体指南检查重要声音信息、字幕及音频描述，不能只勾一个"已有字幕"。
- **可交付 = 各类条件的明确合取**（或经批准的例外处理），不是某个 agent 写的乐观总结。

# 验收记录应包含
见 [交付验收记录模板](/templates/delivery-acceptance-record.md)：文件身份、对应画面与声音版本、导出时间、测量工具及范围、检查结果、试听环境、审核者、保留问题。

# 关系
- 上位主题：[10 AI 影视团队声音协作与交付](/topics/10-ai-team-sound-collaboration.md)
- 技术验收方法与指标边界：[09 声音评价、适配测试与验收](/topics/09-sound-evaluation-acceptance.md)
- 状态链中"已验证"的前提：[声音工作状态链](/frameworks/sound-production-status-chain.md)

# Citations
[1] [10 AI影视团队声音协作 §16 16. 交付验收：每个结论都要能指向实际文件](../../../声音设计理论与方法_二至十/10_AI影视团队_声音协作与交付.md)
[2] [ITU-R BS.1770](/references/itu-bs-1770.md)
[3] [EBU R 128](/references/ebu.md)
[4] [W3C WAI Making Audio and Video Media Accessible](/references/wai.md)

---
type: Framework
title: "固定工作流与 agent 的任务区分"
description: "确定性任务用程序或固定流程；需解释与取舍的任务可引入 agent；需实际感知的任务依赖真实音视频能力；有外部后果的任务需明确授权。"
tags: [topic-10, AI协作, agent, 工作流, 授权]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/sound/声音设计理论与方法_二至十/10_AI影视团队_声音协作与交付.md#2. 什么时候需要 agent，什么时候只需要固定工作流？"
---

# 依据
Anthropic 工程经验文区分**预定义工作流**与**更自主决策的 agent**，并建议从能解决问题的较简单结构开始。这是工程经验，**不是**"某种编排对所有影视项目最优"的实验定律（来源支持，边界明确）。

# 四类任务
| 任务类型 | 处理方式 | 声音制作例子 |
|---|---|---|
| 确定性任务 | 程序或固定流程，不需多模型反复投票 | 读取已知文件元数据、核对时长、检查文件是否存在、列版本依赖、计算拍点 |
| 解释与取舍 | 可引入 agent | 基于剧本与目标提出声画关系候选；比较多个声音命题；整理评审中真正冲突的约束 |
| 需实际感知 | 依赖真实音视频能力 | 没有听音或波形分析工具，就**不能**凭提示词宣称无削波、旁白清晰、情绪达标 |
| 有外部后果 | 需要明确授权 | 付费生成、购买授权、向外部服务上传未公开素材、发布成片；创作同意 ≠ 外部操作授权 |

# 关系
- 上位主题：[10 AI 影视团队声音协作与交付](/topics/10-ai-team-sound-collaboration.md)
- 感知能力要先验证：[声音任务能力矩阵](/templates/sound-task-capability-matrix.md)
- 授权边界：[知识、数据与指令的边界](/principles/knowledge-data-instruction-boundary.md)、[权利对象与批准分离](/principles/rights-objects-separate-from-approval.md)
- 规模选择：[最小版本与扩展版本](/principles/minimal-vs-extended-sound-team.md)

# Citations
[1] [10 AI影视团队声音协作 §2 2. 什么时候需要 agent，什么时候只需要固定工作流？](../../../声音设计理论与方法_二至十/10_AI影视团队_声音协作与交付.md)
[2] [Anthropic, Building effective agents](/references/agent.md)

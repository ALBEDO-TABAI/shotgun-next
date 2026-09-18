---
type: Skill Interface
title: "skill：character-relation-world-model"
description: 人物—关系—世界联合模型的接口：输入材料与模式边界、六步工作流程、YAML 输出模板；只维护真正影响作品和后续执行的关系。
tags: [topic-04, skill, 接口, 人物模型, 输出模板]
timestamp: 2026-09-18T00:00:00Z
source: new-version/script/04_人物行为关系与世界规则.md#十二、skill：character-relation-world-model
---

# 启动条件

人物行为或世界条件不成立、人物依据与双向关系不清、规则与例外需要建立时启动（见总表 [按问题调用模块](/methods/call-modules-by-problem.md)）。

# 输入与边界

- 输入：人物资料、剧本、片段、世界说明或候选构想。
- 分析模式只使用已有材料；创作模式允许新增，但必须标明。
- 只有图像时，不凭服装和表情制造姓名、职业、家庭史或心理诊断。
- 不应自动做：给现实人物诊断或补人生档案。

# 工作流程

1. 列出重要人物与时间范围；
2. 区分直接赋性、他人评价和行动证据；
3. 建立当前任务、信念、策略、资源与代价；
4. 用双向关系分析互动；
5. 检查世界规则与例外；
6. 确认关键选择是否在实际表达中得到支持。

# 输出模板

```yaml
character_id: C-D
scene_id: KEY-02
established_fact: 她收回旧住所备用钥匙
immediate_task: 完成归还并保留来访关系
belief: 直接提出边界可能被理解为疏远
belief_status: 创作假设，需要场景支持
strategy: 解释钥匙失效，然后发出具体邀请
constraint: 她可以决定权限，不能控制父亲感受
observed_change: 双方开始商定来访时间
not_established: 父亲长期观念已彻底改变
world_dependency: 旧钥匙的实际进入权限在本版必须明确
validation_status: 尚未试演
```

不用永久记录所有细小心理状态；只维护真正影响作品和后续执行的关系。`validation_status` 必须来自实际工作，不是填了就算发生。

# 关系

- 上位主题：[本篇枢纽](/topics/04-character-relation-world.md)
- 统一输入 / 输出与状态含义见 [统一 skill 接口](/skills/unified-skill-interface.md)。
- 各步骤对应：[人物三层面](/frameworks/character-three-levels.md)、[行动依据](/frameworks/action-basis-instead-of-trait-list.md)、[双向关系](/frameworks/relationship-as-bidirectional-process.md)、[世界规则](/frameworks/world-rules-four-questions.md)、[最小模型](/methods/minimal-character-world-model.md)。
- 输出中的 belief / world_dependency 交接给 [信息依赖表](/templates/information-dependency-table.md) 与 [阶段 C 联合骨架](/methods/stage-c-joint-skeleton.md)。

# Citations
[1] [04 人物行为关系与世界规则 §十二](../../../04_人物行为关系与世界规则.md)
[2] [skill 接口与调用总表](../../../00_skill接口与调用总表.md)

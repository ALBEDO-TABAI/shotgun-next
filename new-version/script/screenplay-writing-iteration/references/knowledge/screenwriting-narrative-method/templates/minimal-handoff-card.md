---
type: Template
title: 最小交接卡
description: 一场戏交给执行部门时的最小 YAML 说明：必须建立什么、允许开放什么、主要载体、受保护关系、可灵活项、改动后需重查项、证据状态与下一次测试。
tags: [topic-02, 交接, 模板, 制作说明]
timestamp: 2026-09-18T00:00:00Z
source: new-version/script/02_编剧工作与协作贡献建模.md#7. 最小交接卡
---

# 模板

```yaml
scene_id: DOOR-01
version: candidate_B
must_establish: 父亲允许女儿及行李进入屋内
may_remain_open: 双方是否已完全和解
primary_carrier: 事务性指令、误拉、腾出门内位置
protected_relation: 邀请通过实际允许进入得到支持
flexible: 腾出位置的具体动作、镜头数量
recheck_on_change: 删除误拉、加入拥抱、改变音乐语调
evidence_status: 自拟文本，未实拍或测试
next_test: 不提供主题提示的简易走位观看
```

# 字段说明

| 字段 | 含义 | 填写要求 |
|---|---|---|
| scene_id / version | 场景与候选版本标识 | 版本要能对应到修改记录 |
| must_establish | 本场必须让观众获得的理解 | 写结果，不写愿望词 |
| may_remain_open | 本场有意不解决的问题 | 明确写出，避免被下游"顺手"补齐 |
| primary_carrier | 承担意义的主要载体 | 动作、指令、空间等可感知过程，不是情绪标签 |
| protected_relation | 不能无说明破坏的关系 | 保护的是意义关系，不是镜头列表 |
| flexible | 可替换的具体方式 | 允许执行者选择 |
| recheck_on_change | 哪些改动会触发重新检查 | 列出具体改动 |
| evidence_status | 当前证据状态 | 自拟 / 试排 / 实拍 / 已测试，如实填写 |
| next_test | 下一次验证的对象与方法 | 不提供主题提示 |

# 使用说明
- 这是一份可使用的说明格式，**不是已运行的程序或已通过的验收记录**；填了字段不等于状态发生。
- 只用于对意义有影响的关键交接，不要求每个普通镜头都填。
- 接收者应能据此**回述**：理解了什么关系、准备用什么动作完成、哪些要改、保留什么顺序。

# 关系
- 上位主题：[本篇枢纽](../topics/02-screenwriting-work-and-contribution.md)
- 示例来自 [门口一只箱子](../cases/box-at-the-door-screenwriting-work.md)。
- 制作说明"保护关系而非锁死手段"的标准见 [交付物完成标准](../checklists/deliverable-completion-criteria.md)；回述要求见 [合作与作者意图](../principles/collaboration-and-author-intent.md)。
- 跨版本、跨媒介的交接扩展见 [跨版本交接](cross-version-handoff.md)；对白层面的交接见 [对白交接说明](dialogue-handoff-to-execution.md)；受保护关系的完整示例见 [护肤片五个关键关系](../cases/skincare-film-five-protected-relations.md)。
- 字段与 [统一 skill 接口](../skills/unified-skill-interface.md) 的 protected_relations / flexible_execution / next_validation / status 对应。

# Citations
[1] 02 编剧工作与协作贡献建模 §六.7（历史来源定位：`../../../02_编剧工作与协作贡献建模.md`；原文件未随上传包提供）

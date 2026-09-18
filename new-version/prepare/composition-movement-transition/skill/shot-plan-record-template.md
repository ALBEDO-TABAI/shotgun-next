---
type: Template
title: "轻量镜头计划记录结构"
description: "序列/镜头/接缝三级的概念模板（YAML 示例），让 end_state 被相邻镜头与接缝检查消费。"
tags: [模板, YAML, 镜头计划]
timestamp: 2026-09-18T00:00:00Z
source: "构图运镜镜头衔接_知识包/05_联合设计案例与Skill执行规范.md#9"
---

> 设计规范与可填写模板；未宣称已部署、调用或通过验收。

下面是可采用的概念模板，不是某个已实现软件的 API。已知事项填写，未知可以空缺并说明原因；简单场景不需要强迫生成 JSON 或 YAML。

```yaml
sequence_id: A
status: draft
intent: "让开启与使用动作可理解，最后完成完整包装识别"
constraints:
  must_read: ["同一产品身份", "按泵与承接关系"]
  allowed_ellipsis: ["非关键手部移位"]
shots:
  - id: A02
    purpose: "看清保护盖被取下"
    start_state: "右手已抓住盖子，盖子开始向上离开"
    key_change: "泵头显露，盖子被放到台面约定区域"
    end_state: "泵头可用，盖子留在瓶旁"
    framing: "手、盖子、泵头和落点均在可读范围"
    subject_motion: "右手上提后放下盖子"
    camera_motion: "固定"
    trigger: "继承前镜头已经开始的开启动作"
    evidence_status: "planned_not_observed"
    candidates: ["动作开始处切入", "盖子离开泵头时切入"]
transitions:
  - from: A01
    to: A02
    relation: "同一动作继续"
    preserve: ["手别", "产品朝向", "盖子开合阶段"]
    allowed_change: ["景别", "经试剪确认的少量动作省略或重叠"]
    validate: "先整段播放，再检查接缝两侧动作状态"
```

关键是让 `end_state` 真正被相邻镜头和接缝检查消费，而不是写出后再由下游凭空重判。若需要生成工具描述，应由当前确认的镜头计划产生，并回查实际结果；工具请求不能反向充当“已实现”的证据。

# 相关概念
* [为什么分镜表必须同时写“镜内变化”和“镜间关系”](/skill/shot-list-within-and-between.md) — 为什么要这样记录
* [两个镜头之间的“交接约定”](/foundations/shot-handoff-contract.md) — transitions 字段的来源
* [案例 A：二十秒乳液广告，如何避免漂亮但接不起来](/cases/case-a-lotion-ad-20s.md) — 示例数据来自案例 A

# Citations
[1] [05_联合设计案例与Skill执行规范.md §9](../../../构图运镜镜头衔接_知识包/05_联合设计案例与Skill执行规范.md)

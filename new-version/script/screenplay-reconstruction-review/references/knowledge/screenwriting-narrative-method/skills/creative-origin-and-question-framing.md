---
type: Skill Interface
title: "skill：creative-origin-and-question-framing"
description: 起点抽象或方向未定时启动；输入 brief、感受、细节、人物、事实、物件或形式兴趣，输出材料地图、暂定问题、候选形式、代表性段落、未知与测试。
tags: [topic-03, skill, 接口, 创作起点]
timestamp: 2026-09-18T00:00:00Z
source: new-version/script/03_创作起点与具体问题建构.md#十一、skill：creative-origin-and-question-framing
---

# 定位

本包提供的是理论与接口范例，**不是已安装运行的技能实现**。模块名称用于说明分工。

# 输入与启动

- 输入可以是 brief、感受、细节、人物、事实、物件或形式兴趣。
- 信息少时不必追问整个人生背景才开始：先提出暂定解释和两条不同路径，同时标明哪项未知最影响选择。
- 启动条件（总表）：起点抽象或方向未定。

# 操作

1. 拆分题材到形式的六层；
2. 识别原始起点类型；
3. 区分观察、自述、资料与构造；
4. 提出反例问题；
5. 生成真正不同的方案；
6. 为每个方案写代表性场景或段落；
7. 选择下一项研究或原型。

"不同方案"不要求机械凑数量：明确的改编任务可能只需比较两种视角或结尾，不必重做整个题材。

# 输出

```yaml
concept_id: C-02
origin: 一条反复修改的消息
working_question: 她能否为可以延期的请求安排回应时间
premise: 晚间动作已开始，请求并不紧急
form_hypothesis: 单一微事件，不回顾全部职业经历
source_status: 当前为自拟，不是消费者访谈结论
invention: 人物、消息、场景均为创作构造
alternative: 纯过程观察，不以一次回复建立转折
risk: 将结构性压力误写成个人不会拒绝
next_test: 核对期限条件，试读两版信息呈现
```

交付应包括：材料地图、暂定问题、候选形式、代表性段落、未知与测试——而非只是一页主题词。

# 不应自动做什么

- 把个人经验升级成人群洞察（总表"不应自动做什么"）。
- 输入不完整时擅自补全；能局部回答就限定范围，不能回答就列出需要获取的材料。

# 关系

- 上位主题：[本篇枢纽](../topics/03-creative-origin-and-question.md)
- 操作步骤分别展开为：[六层区分](../frameworks/six-levels-subject-to-form.md)、[七种起点](../frameworks/seven-creative-starting-points.md)、[四种材料状态](../frameworks/four-states-of-research-material.md)、[反向提问](../methods/research-as-judgment-changing-questions.md)、[五次转化](../methods/five-transformations-material-to-question.md)、[构想筛选](../checklists/concept-screening.md)。
- 统一输入 / 输出与状态字段见 [统一 skill 接口](unified-skill-interface.md)；按问题调用模块见 [按问题调用模块](../methods/call-modules-by-problem.md)。
- 下游交接：[阶段 A：建立问题、材料与边界](../methods/stage-a-problem-material-boundary.md)、[阶段 B：比较形式](../methods/stage-b-form-and-representative-fragment.md)。
- 形式定位的前置模块：[叙事形式识别 skill](narrative-form-identification.md)。

# Citations
[1] 03 创作起点与具体问题建构 §十一（历史来源定位：`../../../03_创作起点与具体问题建构.md`；原文件未随上传包提供）
[2] skill 接口与调用总表（历史来源定位：`../../../00_skill接口与调用总表.md`；原文件未随上传包提供）

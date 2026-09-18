---
type: Skill Interface
title: "skill：scene-plot-and-rhythm-design"
description: 场景、情节与节奏模块的输入、分析流程、创作流程与场景记录 YAML；非叙事段落允许不适用因果字段，不为填表而虚构剧情。
tags: [topic-05, skill, 接口, 场景设计]
timestamp: 2026-09-18T00:00:00Z
source: new-version/script/05_场景情节与叙事节奏设计.md#十二、skill：scene-plot-and-rhythm-design
---

# 启动条件

场景、连接或节奏出现问题（来自 [模块边界表](../methods/call-modules-by-problem.md)）。

# 输入

- 形式档案、人物与世界条件、当前场景或序列、时长与观看条件。
- **缺少前后文**时，不能断定某处铺垫无用；**缺声音**时，要限制语调与节奏判断。

# 分析流程

1. 确定切分尺度（[统一分析尺度](../frameworks/analysis-units-shot-to-sequence.md)）；
2. 记录进入与离开状态（[进入—作用—离开](../frameworks/scene-entry-process-exit-model.md)）；
3. 识别作用过程；
4. 给段间连接命名（[情节连接类型](../frameworks/plot-connection-types.md)）；
5. 分别标记事件、信息与视听变化，情绪记录为假设或实际反馈（[节奏四层](../frameworks/rhythm-four-observation-layers.md)）；
6. 用小范围删减、换序、延长、改载体比较。

# 创作流程

1. 写下希望被经历的变化（[场景第一问](../frameworks/scene-purpose-and-functions.md)）；
2. 设置实际行动条件（[空间与物件](../frameworks/space-and-objects-in-scene.md)）；
3. 选择必要证据；
4. 安排进入和退出（[场景如何结束](../frameworks/scene-endings.md)）；
5. 估计读取与表演时间；
6. 试写、试排或做视听草稿。

发现前提不成立可以回退，不必等全片写完。

# 输出：场景记录

```yaml
scene_id: MOVE-03
scope: 旧家至门口
before: 女儿认为母亲不愿搬走
process: 准备标记、门宽限制、工具出现、共同拆卸
after: 女儿参与保护并搬运餐桌
causal_relation: 门宽限制要求改变搬运方式
inference_relation: 提前准备支持母亲已经接受搬迁的理解
risk: 工具准备不可读会破坏理解修正
duration_status: 90秒候选，未实测
next_test: 按真实空间和家具进行简易走位
```

# 不应自动做什么

- 用固定幕结构检查所有形式。
- 非叙事段落允许不适用因果字段，改记形式或分类关系。**不为填表而虚构剧情。**
- 交付是"关于作品怎样推进的证据化说明"，不是标准结构合格证。

# 关系

- 上位主题：[本篇枢纽](../topics/05-scene-plot-rhythm.md)。
- 输出字段与 [统一 skill 接口](unified-skill-interface.md) 的 result 结构兼容（status 应为 proposal，直至实际使用）。
- 输入中的"形式档案"来自 [narrative-form-identification](narrative-form-identification.md)；"人物与世界条件"来自 [character-relation-world-model](character-relation-world-model.md)。
- 下游：场景稿的对白互动交给 [dialogue-as-interaction](dialogue-as-interaction.md)。
- 完整示例：[两个人搬走一张餐桌](../cases/moving-a-dining-table.md)。

# Citations
[1] 05 场景情节与叙事节奏设计 §十二（历史来源定位：`../../../05_场景情节与叙事节奏设计.md`；原文件未随上传包提供）

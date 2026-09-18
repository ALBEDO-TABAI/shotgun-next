---
type: Skill Interface
title: "skill：screenwriting-work-and-contribution-map"
description: 编剧工作与贡献地图模块的输入、步骤与输出结构：按六类工作识别关键选择，追踪来源、载体、依赖与实现状态，输出可行动的问题与验证办法；无证据不裁定署名。
tags: [topic-02, skill, 接口, 贡献建模]
timestamp: 2026-09-18T00:00:00Z
source: new-version/script/02_编剧工作与协作贡献建模.md#九、skill：screenwriting-work-and-contribution-map
---

# 定位
本模块是理论与接口范例，**不是已安装运行的技能实现**。启动条件：工作或贡献不清。

# 输入
- 作品或单版剧本、多版本材料、制作记录、当前问题、分析范围。
- 输入决定可回答的层级：
  - 只有成片 → 可分析叙事活动，未必能归属贡献；
  - 只有梗概 → 不能评价未写出的对白自然度。

# 步骤
1. 确认材料与版本。
2. 按六类工作识别重要选择。
3. 追踪来源、载体和依赖。
4. 比较改动怎样改变关系。
5. 核对实际实现。
6. 输出可行动的问题与验证办法。

既要找错误，也要记录**值得保护的有效安排**——只列批评的报告会使修改者无意删除作品最重要的部分。

# 输出结构
```text
工作项ID与适用范围：
改变的叙事关系：
直接材料证据：
作者意图状态：明确自述／推测／未知
贡献者证据：版本／记录／单方回忆／无法确认
实现状态：只在文本／试排／拍摄／当前剪辑保留
依赖哪些前后关系：
谁需要使用本项决定：
允许怎样替换：
修改后要重新检查什么：
```

# 完成与边界
- 未知、不适用、有分歧都是合法结果。
- 不必为每个普通词语建立记录，只追踪影响理解与执行的关键选择。
- 不应自动做：无证据裁定署名或占比。

# 关系
- 上位主题：[本篇枢纽](../topics/02-screenwriting-work-and-contribution.md)
- 步骤 2 依据 [六类核心编剧工作](../frameworks/six-screenwriting-work-types.md)；证据字段依据 [贡献追溯的三层证据](../frameworks/contribution-evidence-three-layers.md)；意图状态字段依据 [合作与作者意图](../principles/collaboration-and-author-intent.md)。
- 输出中的"允许怎样替换 / 修改后重查"与 [最小交接卡](../templates/minimal-handoff-card.md) 字段对应；等价判断见 [跨抽象层等价检查](../methods/cross-abstraction-equivalence-check.md)。
- 与其它模块的统一输入输出与状态含义见 [统一 skill 接口](unified-skill-interface.md)；按问题调用模块见 [按问题调用模块](../methods/call-modules-by-problem.md)。

# Citations
[1] 02 编剧工作与协作贡献建模 §九（历史来源定位：`../../../02_编剧工作与协作贡献建模.md`；原文件未随上传包提供）

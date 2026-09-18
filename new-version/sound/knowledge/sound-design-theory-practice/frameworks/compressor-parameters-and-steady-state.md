---
type: Framework
title: "压缩器参数与稳态算例"
description: "threshold／ratio／knee／range 与 attack／release 的含义及其实现差异；硬拐点 −24 dB、3:1、输入 −12 dB 的稳态算例得 −20 dB，但不能预测真实瞬态。"
tags: [practice-m6, 压缩, 动态处理, 参数]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/sound/声音创作与制作_实践知识包/声音创作与制作_实践知识包.md#6.5 压缩器：先说它要改变什么，再调参数"
---

# 原则
先说压缩**要改变什么**，再调参数。

# Schema：普通向下压缩的参数
| 参数 | 含义 | 注意 |
|---|---|---|
| threshold | 从什么检测电平开始增益控制 | — |
| ratio | 超阈值部分的压缩关系 | — |
| knee | 过渡形态 | — |
| range | 限制最大增益变化 | 并非所有产品都有 |
| attack／release | 增益变化的**时间行为** | 不是"等待若干毫秒然后瞬间压低"；定义、曲线、节目依赖性看具体工具与模式 |

不同产品与模式实现不完全相同（来源支持：官方手册）。[2][3]

# Examples：稳态算例（仅理解用）
硬拐点、阈值 −24 dB、3:1，持续输入 −12 dB，忽略时间响应与补偿增益：

- 超阈值 12 dB → 输出超阈值 12/3 = 4 dB → 输出 ≈ **−20 dB**，压低约 **8 dB**。

该算例**不能**预测真实语音瞬态经过任意压缩器的每个采样值。

# 关系
- 上位主题：[实践包主枢纽](/topics/p-sound-creation-production.md)
- 可执行试听流程：[压缩试听试验](/recipes/compression-listening-test.md)
- 外部检测信号：[侧链避让](/methods/sidechain-ducking-for-voiceover.md)
- 表达强 ≠ 电平高：[04 声音描述语言](/topics/04-sound-description-language.md)

# Citations
[1] [实践知识包 §6.5](../../../声音创作与制作_实践知识包/声音创作与制作_实践知识包.md)
[2] [S22 · FabFilter Pro-C 3 Dynamics controls](/references/s22.md)
[3] [S23 · FabFilter Pro-C 3 Time controls](/references/s23.md)

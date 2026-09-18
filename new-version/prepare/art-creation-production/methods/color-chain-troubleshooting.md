---
type: Method
title: "颜色不对时先查链路，再决定重刷"
description: "颜色问题可能发生在物体、照明、摄影、处理与观看；先核样片与批准对象、同光同机位比较、再查输入解释与显示路径，最后才物理修改；ACES 区分输入／Look／输出，但不要求所有项目采用 ACES。"
tags: [色彩, 链路, 诊断, ACES]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/art-director/美术创作与制作知识包_v2/05_测试现场优化与回修.md#5. 颜色不对时，先查链路，再决定重刷"
---

# 排查次序

1. 样片本身是否与批准对象一致：批次、面层、涂层状态、表面方向。
2. 同一光和机位下与保留样片比较。
3. 物理条件未变而不同软件或导出版本差别明显 → 查图像解释与显示路径。
4. 只有差异确实来自物面或环境时，再做物理修改。

# 例：“工坊看着米白，监看偏绿”

同一块样片与主体同框，不立刻换颜料；固定白平衡与照明后查看；核对素材是否按正确输入处理；比较同一输出的两台观看设备。

# 边界

- ACES 官方文档将输入变换、创意 Look、输出变换分开，输出面向具体设备与观看条件；启发是**色彩链路必须说清**，但不是所有项目必须采用 ACES。
- “去掉所有处理”不是绝对中立图像；保留一条技术检查视图与一条创意预览有助于定位，具体由项目影像人员确定。
- 资料不足时写“当前只能在这套查看条件下比较”，不给跨设备绝对正确的色彩结论。

# 关系

- 上位主题：[05 测试、现场优化与回修：从“这版不够好”到定位、改变、验证](/topics/05-testing-onset-optimization-revision.md)
- 故障：导出后感觉全变了：[十二种常见故障与第一项有用动作（含升级路线条件）](/checklists/twelve-common-faults-first-action.md)
- 实体、数字与后期分工模板：[模板八｜实体、数字与后期的效果分工](/templates/t08-physical-digital-post-division.md)

# Citations
[1] [05 测试、现场优化与回修 · 5. 颜色不对时，先查链路，再决定重刷](../../../美术创作与制作知识包_v2/05_测试现场优化与回修.md)
[2] [S36 Input Transforms](/references/s36-aces-input-transforms.md)
[3] [S37 Look Transforms](/references/s37-aces-look-transforms.md)
[4] [S38 Output Transforms](/references/s38-aces-output-transforms.md)

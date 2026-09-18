---
type: Framework
title: "用镜头几何估计搭建边界（含教学算例）"
description: "θh = 2·arctan(s/2f)，W(d) ≈ d·s/f；36mm/50mm 时 4m 主体面宽 2.88m、6m 背景面宽 4.32m，平移 ±0.4m 后联合宽 5.12m——主体空间够不代表背板够；公式只作早期预算。"
tags: [镜头几何, 视场, 搭建边界, 教学算例]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/art-director/美术创作与制作知识包_v2/02_空间设计与搭建转译.md#4. 用镜头几何估计搭建边界"
---

# 关系式（理想直线投影）

```text
θh = 2 × arctan(s / (2f))
W(d) ≈ d × s / f      （垂直于光轴、距投影中心 d 的平面可见宽度）
```

s = 有效传感器宽度，f = 焦距。仅作早期预算，不考虑具体镜头畸变、近焦有效焦距变化和非对称裁切；微距产品拍摄应直接量测实际取景。

# 教学算例（教学假设，非标准）

| 条件 | 结果 |
|---|---|
| s = 36 mm，f = 50 mm，主体平面 4 m | 可见宽 ≈ 2.88 m |
| 背景平面 6 m | 可见宽 ≈ 4.32 m |
| 相机只平移不旋转，左右各 0.40 m | 背景联合宽 ≈ 4.32 + 0.80 = 5.12 m |
| 本算例人为加左右各 0.20 m 余量 | 候选宽 5.52 m（**0.20 m 不是行业标准**） |

实际平移伴随摇摄、前后移动或防抖裁切时，要逐个姿态重新计算或预演。

# 价值

暴露成本来源：移动幅度和背景距离增加可能要求更多背板。可以比较拉近背景、限制移动或改机位，而不只扩大整套搭建。

# 关系

- 上位主题：[02 空间设计与搭建转译：把画面意图变成能拍、能用、能安装和修改的空间](/topics/02-space-design-build-translation.md)
- 相机位置与焦距分开讨论：[相机位置与焦距分开讨论](/principles/camera-position-vs-focal-length.md)
- 横竖版裁切：[横竖版不能只看安全框](/methods/aspect-ratio-crop-check.md)
- 镜头包络：[镜头包络：把规定镜头姿态下的所有可见边界叠在一起](/frameworks/shot-envelope.md)

# Citations
[1] [02 空间设计与搭建转译 · 4. 用镜头几何估计搭建边界](../../../美术创作与制作知识包_v2/02_空间设计与搭建转译.md)
[2] [S31 Understanding Focal Length and Field of View](/references/s31-edmund-focal-length-fov.md)

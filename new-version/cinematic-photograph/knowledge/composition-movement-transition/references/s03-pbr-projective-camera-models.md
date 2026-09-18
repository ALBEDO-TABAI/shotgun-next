---
type: Reference
title: "S03｜Pharr、Jakob、Humphreys：Projective Camera Models"
description: "PBR 第四版投影相机章节，支撑平移/转动/焦距的几何区别与推拉变焦近似条件。"
tags: [技术文档, 投影几何, 相机模型]
resource: https://www.pbr-book.org/4ed/Cameras_and_Film/Projective_Camera_Models
timestamp: 2026-09-18T00:00:00Z
source: "构图运镜镜头衔接_知识包/06_研究来源与证据边界.md#source-s03"
---

# 书目信息

| 字段 | 内容 |
|---|---|
| 类型 | 作者公开的技术著作章节。 |
| 著作 | Physically Based Rendering: From Theory to Implementation, Fourth Edition。 |
| 章节 | Cameras and Film / Projective Camera Models。 |
| 地址 | `https://www.pbr-book.org/4ed/Cameras_and_Film/Projective_Camera_Models` |

# 核读范围

投影相机、透视与相机坐标关系的公开正文。

# 支持内容

平移、转动、投影与焦距的区别；用理想透视关系说明推进不等于变焦，以及推拉变焦维持主体尺度的近似条件。

# 使用边界

理想模型不直接包含所有真实镜头的畸变、呼吸、机械耦合或后期变化；不从模型推出任何固定情绪意义。文中的应用式推导和拍摄候选为本包综合。

# 被本包引用于
* [C04｜景别、比例与关系的可读尺度](/composition/c04-shot-scale-readable-proportion.md)
* [C05｜前中后景与深度分层](/composition/c05-depth-layering.md)
* [C09｜俯仰视点、观看高度与参照物](/composition/c09-camera-height-angle-reference.md)
* [C14｜俯视、平铺与拓扑关系](/composition/c14-top-down-flat-lay-topology.md)
* [M02｜水平摇摄 Pan：沿方向依次组织信息](/camera-movement/m02-pan.md)
* [M03｜俯仰摇摄 Tilt：沿垂直关系显露](/camera-movement/m03-tilt.md)
* [M04｜推进 Dolly/Track In：改变接近的过程](/camera-movement/m04-dolly-in.md)
* [M05｜拉远 Dolly/Track Out：让对象进入更大的关系](/camera-movement/m05-dolly-out.md)
* [M06｜横移 Truck/Track：通过视差和遮挡变化观察](/camera-movement/m06-truck-lateral.md)
* [M10｜变焦 Zoom：让选择的动作可见](/camera-movement/m10-zoom.md)
* [M11｜推拉变焦 Dolly Zoom：保持主体尺度而改变背景关系](/camera-movement/m11-dolly-zoom.md)
* [M16｜焦点转移 Rack Focus：相机不动也能改变信息开放](/camera-movement/m16-rack-focus.md)
* [跨切点需要区分的几个方向](/transitions/directions-across-the-cut.md)
* [理论支点五：相机运动的物理变化与心理解释必须分层](/foundations/theory-movement-physical-vs-interpretation.md)
* [术语拆分：设备、轨迹和表达分列](/foundations/camera-terminology-layers.md)

# Citations
[1] [06_研究来源与证据边界.md §S03](../../../构图运镜镜头衔接_知识包/06_研究来源与证据边界.md)
[2] [Pharr、Jakob、Humphreys：Projective Camera Models](https://www.pbr-book.org/4ed/Cameras_and_Film/Projective_Camera_Models)

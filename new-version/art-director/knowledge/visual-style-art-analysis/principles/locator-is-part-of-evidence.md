---
type: Principle
title: "定位是证据的一部分：陈述必须绑定到对象"
description: "借 W3C Web Annotation 的“内容与目标分离、片段定位”思想；纸上写“第三张图，产品左侧叶片”也有效，没有资源时不编造时间码或文件名。"
tags: ["part-02", "part-08", "定位", "标注", "证据"]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/art-director/视觉美术分析知识包/二_视觉观察与形式证据.md#二、6. 视觉标注：定位是证据的一部分"
---

# 依据

W3C Web Annotation Data Model 将注释内容与其目标区分，并提供定位特定资源片段的机制（文本位置、图像区域、视频时间段）。

# 原则

- 谈论“这个反射”时说明在哪张图、哪个区域；谈论“空间突然展开”时说明哪个版本、哪个时间区间。
- 日常拆片不需要部署语义网系统：“第三张图，产品左侧叶片”也有效；多版本、多人协作或程序读取使指代不清时，才需要更严格的编号和坐标。
- 定位精度应跟随证据能力：文本用段落或行号；图像用相对位置、区域或坐标；视频用版本和时间区间。
- 没有精确坐标时先用清楚的位置描述；**没有实际视频时，不可编造时间码**；`frame_123.jpg` 看起来像文件名，不代表文件存在。

# 边界

简化记录不是对完整标准兼容性的声明。

# 关系

- 所属篇章枢纽：[二 视觉观察与形式证据](/topics/02-visual-observation-and-formal-evidence.md)
- 所属篇章枢纽：[八 分析沉淀与知识复用](/topics/08-knowledge-capture-and-reuse.md)
- 观察记录中的 locator 字段：[单条观察记录（visual_observation）](/templates/visual-observation-record.md)
- 第八篇：原始资源与派生资源分开：[原始资源与派生资源分开；定位精度跟随证据能力](/principles/original-vs-derived-resources.md)

# Citations

[1] [二 视觉观察与形式证据 · 二、6. 视觉标注：定位是证据的一部分](../../../视觉美术分析知识包/二_视觉观察与形式证据.md)
[2] [八 分析沉淀与知识复用 · 二、2. 标注：评论必须绑定到明确的目标](../../../视觉美术分析知识包/八_分析沉淀与知识复用.md)
[3] [八 分析沉淀与知识复用 · 八、定位精度应跟随证据能力](../../../视觉美术分析知识包/八_分析沉淀与知识复用.md)
[4] [R28｜Web Annotation Data Model](/references/r28-w3c-web-annotation-data-model.md)

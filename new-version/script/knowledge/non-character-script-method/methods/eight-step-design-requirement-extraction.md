---
type: Method
title: "从正文提取设计需求的八步操作"
description: "圈名词、圈动词补条件、建立对象身份、区分状态／动作／关系条件、写清下游自由、写最小可用性判断、双向回看、保留待解决项。"
tags: [topic-05, 设计需求, 提取, 双向追溯, 交接]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/script/非人物初步剧本_六专题深化版/05_初步剧本写作与设计需求交接.md#8. 如何从正文提取设计需求：八步实际操作"
---
# 要点

以下示例均取自原创虚构的 [「一页」V1 正文](/examples/yiye-lamp-v1-script.md)。

| 步 | 做什么 | 「一页」示例 | 防止什么 |
|---|---|---|---|
| 1 | **圈出名词，但不要立刻建模** | 产品、灯头、立柱、底座、铰链、按钮、手、书、纸面、桌面、名称——其中既有资产，也有部件、状态和文字 | 先分清层级，避免把同一灯头生成成三个独立物件 |
| 2 | **圈出动词，补出不可见条件** | 抬起依赖铰链与手部接触；按下依赖按钮界面；转向纸面依赖局部与整体对应；字卡出现依赖准确文字层 | 动作只有结果、没有成立条件 |
| 3 | **建立一个对象身份** | D01 管整灯身份，D02 管同一灯的姿态，D03 管按钮与发光状态——它们不是三盏灯；对象标识可为 `LAMP-01`，部件保持从属 | 每个镜头再定义一套外观 |
| 4 | **区分静态状态、动作条件和关系条件** | 工作姿态是状态；绕单轴转动是动作条件；手不得遮住铰链是可见关系；同一书页重新定位是披露关系 | 把一切压成「提供三视图」 |
| 5 | **写清下游自由** | 桌面材质可选；书页可有非精确排版（需可读正文时另审文字）；镜头可变，只要局部与整体关系成立 | 必须与可选不分，美术无法真正提案 |
| 6 | **写最小可用性判断** | 「能够展示收拢、中间、工作三个状态且关节身份一致」回答 D02 是否可用；「看起来高级」不是接口验收 | 验收只挑错，不证明它能支撑所选表达 |
| 7 | **双向回看** | 从 B02 追到 D02，能否找到动作条件？从 D09 追到 B04／B05，能否知道为什么需要局部对应？ | 无使用位置的需求是额外负担；无设计支持的关键节拍只是纸面愿望 |
| 8 | **保留待解决，而非假装完成** | 手部动作尚无合适方案，就标为待设计或待验证，并写清下一责任人 | 因为列进了表，就声称资产已有且可用 |

# 适用边界

- 双向对应的思想借自 NASA 需求管理中的追溯做法 [2]；本包**只迁移最小对应思想**（每个关键需求知道为什么存在、谁使用、怎样判断可用），不移植航天工程的完整管理制度。
- 把「资产清单」扩展为「对象、状态、行为、关系、可见性与准确文字」的需求，是本项目的工作格式，不是来源共同验证出的标准 [3][4]。

# 关系

- 上位主题：[05 初步剧本写作与设计需求交接](/topics/05-script-writing-and-design-handoff.md)
- 第 2 步的动词清单见 [可写句法](/methods/writable-sentence-syntax.md)。
- 产出示范：[V1 设计需求清单 D01–D10](/examples/yiye-lamp-v1-design-requirements.md)；单条需求的展开：[D02 局部详单](/examples/d02-requirement-detail-sheet.md)。
- 第 4 步最容易漏掉的一类：[常漏的可见性与关系需求](/checklists/often-missed-visibility-and-relation-requirements.md)。
- 第 8 步的状态标记见 [设计状态与交付状态](/frameworks/design-status-vs-delivery-status.md)。
- 第 7 步的双向关系在改稿时必须同步维护：见第 06 篇 [变更消费与更新回执](/methods/change-consumption-and-update-receipt.md)。
- 填写格式见 [初稿与设计需求模板](/templates/draft-and-requirement-template.md)。

# Citations

[1] [05 初步剧本写作与设计需求交接 §8（依据见 §2）](../../../非人物初步剧本_六专题深化版/05_初步剧本写作与设计需求交接.md)
[2] [S10｜NASA：6.2 Requirements Management](/references/s10-nasa-requirements-management.md)
[3] [S02｜Karana 等：Material Driven Design](/references/s02-karana-material-driven-design.md)
[4] [S17｜Ordinary Folk：Our Motion Design & Animation Process](/references/s17-ordinary-folk-process.md)

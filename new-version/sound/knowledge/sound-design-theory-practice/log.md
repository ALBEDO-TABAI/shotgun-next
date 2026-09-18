# Directory Update Log

## 2026-09-18
* **Initialization**: 从 `new-version/sound/声音设计理论与方法_二至十/`（《一.md》、02–10 九篇、研究方法与来源索引、阅读索引）与 `new-version/sound/声音创作与制作_实践知识包/`（主文、README、exercises/ 下三个 MIDI、生成脚本与 validation.json）提炼，使用 okf-bundle skill 建立本包。来源只读，未改动。目录按 type 划分：topics / frameworks / methods / principles / checklists / templates / cases / skills / exercises / recipes / references。
* **Creation**: 共 407 个概念（Topic Guide×12、Framework×90、Method×61、Principle×60、Checklist×18、Template×30、Case Study×51、Skill Interface×11、Exercise×5、Production Recipe×4、Reference×65），包内关系链接约 2600 条、回源引用 400+ 条，校验 CONFORMANT、无坏链。
* **Creation**: 每篇理论源文档对应一个 [主题枢纽](/topics/) 与一个 [Skill 接口](/skills/)；实践包由 [主枢纽](/topics/p-sound-creation-production.md) 按七个生产模块、贯穿案例、迁移、skill 规范与练习组织，并有 [统一 skill 接口](/skills/skill-sound-creation-production.md)。跨包证据约定见 [来源使用与证据边界总原则](/principles/source-use-and-evidence-boundaries.md)。
* **Naming**: 理论包 07 的设计层案例用 `shampoo-ad-*`，实践包的制作层贯穿案例用 `practice-shampoo-*`，两者互相链接并注明时间假设不同（07：3 s 起 12 小节；实践包：约 1.525 s 起 14 小节）。References 以理论包来源 ID 小写为 slug、实践包用 `sNN`；两包重合的 BER/S02、WIT/S08/S09、EBU/S26 合并为同一 Reference。
* **Verification**: 在临时目录重跑 `exercises/generate_midi.py`，三个 MIDI 的 SHA-256 与 `validation.json` 一致，旋律音列与 [MIDI 练习](/exercises/midi-four-bar-motif-comparison.md) 所述一致；仅限符号层，未渲染或试听。
* **Review needed**: 各篇标注"本包综合"的工作模型是否升级为团队正式口径（四个声音世界、八轴标注、七类功能、多轴适配矩阵、同步三级／入点三位置／四种留白、保留—偏离—新关系、五层证据、六个评价面向与缺陷四级、状态链与角色边界、七个生产模块、最低必要保真度）；两套洗发水案例的时间假设是否统一；参数起点（录音距离、预延迟、尾长、侧链约 2 dB 等）不得被下游当成预设；权利与 M&E／分轨定义需法务与接收方合同核对。
* **Not done**: 未访问 references 的 `resource` 链接确认可达；01 文献地图补充的 6 项来源（Chion、Gaver、Bregman、SFU 手册、Thom Screenwriting、Shams）源文未给链接，`resource` 待补；Schaeffer 等仅被提及的学者未建 Reference；无任何受众试验、音频渲染或 DAW 导入。

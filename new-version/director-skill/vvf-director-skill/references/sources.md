# 来源与证据口径

查阅日期：2026-09-09；第三轮补充 2026-09-12。这里解释知识的根据，不要求每次创作都读。本文及风格卡中的工作流程、示例和选择表是 VVF 综合设计，未经过大规模创作效果实验；引用不是对整套技能的科学认证。

## 证据层级

**事实/技术定义**用于纠正具体错误；**原始研究**只有给定样本和测量范围；**职业实践**提供专业分工与可执行经验；**作品观察**描述真实看见的选择；**创作启发**是本包提出的可修改方案。它们不能互相替代。

另外两类只在 AI 生成任务出现：**当期参数**是模型版本、字数上限、句柄语法、最长秒数、价格、成功率，必须带日期，过期即失效；**项目设定**是某个项目的口味、角色、空间与连续性决定，只在该项目有效，记录方式见场记技能。两者都不写进通用规则。

## 有限学术支持

详细出处、访问范围、样本与限制集中保存在[研究与视觉来源](style-sources.md)，避免重复整份摘要。

| 资料 | 用在何处 | 不用于什么 |
|---|---|---|
| [Smith 2012：注意与电影连续性](style-sources.md#a01) | 切前注意、切后预期 | 给所有影片统一轴线或镜长 |
| [Magliano & Zacks 2011：剪辑与事件分段](style-sources.md#a02) | 区分动作事件与剪辑边界 | 推出所有故事固定分段法 |
| [Hasson等2008：Neurocinematics](style-sources.md#a03) | 限制神经同步指标的解释 | 证明艺术价值或观众一定喜欢 |
| [Mital等2011：动态画面注视](style-sources.md#a04) | 提醒检查竞争性运动；仅摘要核验 | 宣称运动总能控制每个观众 |
| [Mobbs 2006 / Cao等2024：库里肖夫效应](style-sources.md#a05) | 情境与反应镜头的试剪假设 | 把脸部动作当真实内心证据 |
| [Jonauskaite等2020：颜色情绪关联](style-sources.md#a07) | 颜色联想需语境与文化边界 | 固定“某色必然导致某情绪” |

## 技术与职业来源

### T01 — ARRI / Bill Holshevnikoff

[ARRI Lighting Handbook，第四版2016，PDF](https://www.arri.com/resource/blob/83996/409091c612f371b0c68b41d9dcb636db/arri-lighting-handbook-english-data.pdf)。已读印刷页5–17的光质、色彩、主辅光和反射部分。取其光质/阴影及控制的有限技术说明，不沿用其中产品推荐或浅景深等审美偏好作为普遍标准。用于[光色材质](lighting-colour-material.md)。

### T02 — Nikon

[Understanding Focal Length](https://www.nikonusa.com/learn-and-explore/c/tips-and-techniques/understanding-focal-length)，页面标更新2025-12。已读焦距定义、视角/放大率与画幅对照。仅用来分离焦距和取景范围；其“接近人眼”等通俗描述不被当精确视觉科学。用于[镜头设计](shot-design.md)。

### T03 — Kodak

[VISION3 500T 5219/7219 技术资料，PDF](https://www.kodak.com/content/products-brochures/motion-picture/KODAK-VISION3-5219-7219-brochure.pdf)，文件版次未明确。已读第1页曝光与色彩平衡。只核实500T钨丝灯平衡等产品事实，不能从片种名字确定一部作品最终色调。未据此推荐当前购买或用量。

### T04 — British Film Designers Guild

[Job Roles Explained](https://britishfilmdesigners.com/resources/job-roles-explained/)，页面日期未明确。已读美术、概念设计、分镜、研究、布景等岗位说明。用于区分方向设计、制作实施与分镜的协作；本包 addon 的合并/拆分是本次设计选择，不宣称行业只有这些岗位。

## 第二轮表演证据复核

第二轮补核：[Barrett等2019，Emotional Expressions Reconsidered（作者托管PDF，含勘误）](https://affective-science.org/wp-content/uploads/2024/04/barrett-et-al-2019-emotional-expressions-reconsidered-challenges-to-inferring-emotion-from-human-facial-movements.pdf)，DOI 10.1177/1529100619832930。复读摘要与讨论，支持[表演调度](performance.md)区分面部动作和内心推断；不等于表情毫无信息，也不证明某种表演配方更好。

## 第三轮：AI 生成方法的来源

2026-09-12 吸收两份外部技能的方法，未做生成对照实验，全部按职业实践或创作启发使用：

- **Leos 六部门导演组技能 v1**（作者 2026-08-29 分享包整理，仓库名 leos-six-department-directing-team-skill-v1）。其角色权限、状态机、镜内生态、参考单一职责、空间语义锚点、尺度契约、审片分级、返工路由、三本账、单变量迭代和 P/O/C 分类进入[提示词编译](prompt-compilation.md)、[生成审片](generation-review.md)、[空间与状态](space-and-continuity.md)、[表演调度](performance.md)、[交接与续编](collaboration-and-revision.md)。它引用的十三次内部会议只有匿名编号，不可独立访问，因此只算职业实践；它引用的 Runway、Google Veo 提示指南属供应商文档，本次未重新访问，按当期参数对待；它的 5000 字上限、纯文本格式、`@image` 句柄、强调符号是特定模型与团队做法，没有作为通用规则继承。
- **图像反推描述技能**（image-reverse-describe）。其坐标系、深度层四项、遮挡序、主体定位、光线六要素、固有色与光染色、材质光学签名、取证句式、可逆性与一致性自检、长描述转换规则进入[帧描述规范](frame-description.md)、[参考研究](reference-reading.md)、[光色材质](lighting-colour-material.md)。它依据的图像深度线索属视知觉常识，“描述先于判断”属艺术批评教学惯例，材质签名属基于物理渲染的通行说法；该技能未附一手出处，本包也未补，因此只作方法约定。

用户对某项目的口味、模型经验（如“该模型忽略末尾禁止项”）默认记为项目设定或当期参数，先有两个独立案例再考虑进入通用文件。

## 用户给定材料如何被使用

小墨分镜稿提供了画面具体性、光色材质和连续性问题意识；OKF参考提供概念与目录索引组织；三个补充技能提供编剧、人物状态、参考卡及分镜交接；idea-1提供职业分工，idea-2提供观察/改造/执行表达的分离。原文的固定比例、情绪公式、伪精度和供应商保证没有继承。

源项目审计保存在整个交付目录的研究记录中，属于建设证据，不是独立使用本技能的依赖。运行时所有必要方法都在本文件夹内。

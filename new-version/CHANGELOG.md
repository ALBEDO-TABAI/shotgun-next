# 变更记录

## 2026-09-12 · 新版（基线：2026-09-09 旧版包）

方案依据：`../../planning/2026-09-12-skill-upgrade-plan-leos-and-image-reverse.md`。方法来源：Leos 六部门导演组技能 v1、图像反推描述技能；证据边界见导演技能 `references/sources.md` 第三轮。

### 导演技能 `director-skill/vvf-director-skill`

新增：

- `references/frame-description.md`：帧描述规范。
- `references/prompt-compilation.md`：提示词编译。
- `references/generation-review.md`：生成审片与最小返工。
- `assets/video-prompt-skeleton.txt`：参数化的生成单元骨架。
- `scripts/validate_prompt.py`：字段、编号、句柄声明、字数与占比检查；上限默认不限。
- `examples/ai-generation-handoff.md`：从分镜到生成单元再到审片的完整例。

修订：

- `SKILL.md`：路由表增帧描述、提示词编译、生成审片三行；核心工作法加道具与动作状态、每个可见角色有任务、参考一项一职；约束层级加“工具参数是带日期的当期参数”。试用后修订版 4935 字节。
- `references/directing.md`：增一句导演命题；增“节拍与调度状态”。
- `references/performance.md`：增“刺激与时序”“生成表演的常见失真”；台词一节加重音与停顿的行为。
- `references/space-and-continuity.md`：“最小空间记录”改为“锚点与契约”（观看方向、唯一语义锚点、关系图契约、可行性门、尺度契约、人物与环境光）；增“镜内生态”“连续性等级与比较口径”；追踪表加状态机；动作一节加重量与危险感的地理证据。
- `references/shot-design.md`：景别落成占比与落位；运动写起点、触发、速度曲线、落点；层次一节改用前景/中景层/背景与遮挡序；生成单位一节指向提示词编译。
- `references/lighting-colour-material.md`：方向用钟点加高低；增固有色与光染色；增“材质由光学行为写”；光学效果只留一至两项主导；人物穿越光区。
- `references/reference-reading.md`：三种句子改为结论加依据的固定句式；读图顺序升级并指向帧描述规范；有图像反推技能时直接用其结果。
- `references/adaptation-and-coverage.md`：四层拆解的观察层引用帧描述规范；复刻时记每个源镜头的观看任务，抽象段与局部段不得被换成整体展示。
- `references/delivery-formats.md`：快速分镜表建议写主体占比与落位；AI 执行一节缩为入口并指向编译与帧描述；示例链接加生成交接示例。
- `references/quality-review.md`：开头分流到生成审片。
- `references/collaboration-and-revision.md`：角色表增场记与提示词编译两行；增冲突书写格式与各角色边界；增“多岗逐镜审稿（可选）”。
- `references/sources.md`：证据层级增当期参数与项目设定；增第三轮来源说明。
- `references/styles/observational.md`、`references/styles/narrative.md`：两处深度层的“中景/后景”改为“中景层/背景”。

### 新增 addon `addon/vvf-script-supervisor`

`SKILL.md`；`references/continuity-protocol.md`、`references/ledgers.md`、`references/knowledge-cards.md`、`references/sources.md`；`assets/continuity-ledger.csv`、`assets/prompt-version-log.csv`、`assets/take-log.csv`、`assets/project-style-profile.json`；`examples/keys-take-log.md`。

### 其他 addon 修订

- `vvf-cinematographer/references/camera-and-coverage.md`：增“承托与速度曲线”。
- `vvf-cinematographer/references/lighting-design.md`：增“光向写法与光学效果”。
- `vvf-cinematographer/references/handoff-and-tests.md`：输出块增运动四要素、接镜策略与禁止项、验收条件；交给生成时的字段归属。
- `vvf-character-designer/references/media-and-realization.md`：关键帧写尺度、落位、遮挡；一致性失败表增传代劣化行。
- `vvf-art-director/references/spaces-and-props.md`：场景卡增空间锚点与主视角；唯一语义锚点写法；人群空间检查逐人任务。
- `vvf-art-director/references/realization.md`：生成描述先写尺度与落位；参考单一职责与传代劣化。
- `vvf-editor/references/edit-thinking.md`：生成素材返修先看剪辑可解，好表演优先保护。
- `vvf-screenwriter`、`vvf-producer`、`vvf-sound-director`：未改动。

### 有意不做的

- 不设 5000 字硬上限、不禁 JSON、不固定 `@image` 句柄、不用强调符号：均为当期参数或项目做法。
- 不要求生成前的口令式授权：保留“先定案后编译”原则。
- 六角色乘每镜的全覆盖审稿只作可选模式。
- 不新增“表演指导”“镜内执行导演”“提示词导演”入口：方法并入导演与角色技能。
- 不复制两份外部技能进本包。

### 未验证

本版做了结构校验（入口与参考大小、链接、可达性）、示例与试用提示的结构校验、两轮独立文本试用（见下节与 `validation/README.md`）；没有做生成对照实验，也没有人类第三方试用。应用接入时需刷新运行资源清单，旧任务不按新版本解释。

### 2026-09-12 · 两轮独立试用后的修订

由两位未参与编写的试用者分别做导演编译任务与场记三本账任务（记录在 `validation/results/trial-a`、`trial-b`），按他们记录的真实缺口修文件，不为每个案例加铁律：

- `prompt-compilation.md`：区分“提交单位”（逐单元调用的工具按每次提交算字数与参考数）与整包；资产表增产品或道具参考；只有一侧手部参考时的声明；两段式回填连续性帧与参考名额；编译时可撤回假设与退回负责角色的分界；首帧取单元开始时刻并给出生图提示的落点；句柄编号按上传顺序；产品面与主光的关系进检查门；检查门措辞去掉无上下文的指代；占比阈值与脚本一致。
- `frame-description.md`：材质加磨砂与半透明体；归一化坐标的两处用途说法统一；外部技能改为“若另外安装”。
- `assets/video-prompt-skeleton.txt`：镜头总数与时长帧率拆成两行；手部或局部镜头的表演口径；使用说明去重。
- `scripts/validate_prompt.py`：新增 `--per-shot` 逐单元提交量与 `--max-handles` 句柄数量检查；文档说明硬字段是骨架子集。
- `SKILL.md`：路由表指到示例；编译或审片任务的加载预期。
- `space-and-continuity.md`、`generation-review.md`：等级由是否被后续镜头消费决定；图生视频记过程漂移；导演未裁时的建议结论。
- 场记 addon：状态枚举统一为讨论中、待审、已批准、已生成、已废弃；知识类型统一为原则、启发、当期参数、项目设定；候选字段统一叫“知识卡候选”；三份 CSV 改为每行一项并加基线来源、过程观察与时间码、结论来源列；等级判定规则（谁定关键、光向、动作因果）；只有他人观看记录与末帧无人报告的处理；修法加只改一项重生成；多处缺陷的先后；`status` 补 draft/superseded；档案的 department 枚举改用 VVF 角色词；示例改成版本账与 Take 账逐条互指。

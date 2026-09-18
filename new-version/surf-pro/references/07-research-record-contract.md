# 研究记录合同 · schema_version 2.0

只在用户需要可复用资料包、审计或跨 agent 交接时使用。普通聊天不要求生成 JSON。`templates/research-record.json` 是空白教学模板，不能当作完成的调研。

## 1. 一个记录，不再建互相竞争的账本

`research-record.json` 是该次归档中问题、来源、结论和延展路由的结构化事实记录。报告是它的阅读视图，不另设相互矛盾的来源等级、结论状态或任务完成状态。同一来源只建一个 S 项；同一结论只建一个 C 项，必要时关联多个问题。

先更新记录，再使报告与它一致。脚本不能读取报告语义，因此“记录和报告一致”仍需人工/agent 复核。日常短答可以只在回复中保持这些关系，不要求为了合同造文件。

所有对象的下列字段均须存在；无内容的集合使用 `[]`。不添加未定义字段。可空字符串、可空日期和哈希的例外见下文。增加正式字段须升级合同和校验器，不通过隐藏字段维护第二套状态。

## 2. 顶层与任务范围

| 字段 | 类型与用途 |
|---|---|
| schema_version | 字符串 `2.0`。不同于 skill 发布版本 `2.0.0`。 |
| research_id | 非空字符串，识别当前一次研究，不要求特定编码。 |
| is_example | 布尔值。教学/测试为 `true`；真实记录为 `false`。不能只改此值就把示例变成真实证据。 |
| brief | 下表任务对象。 |
| questions / sources / claims / extensions / queries / assets | 对象数组；不使用时为空。 |
| completion | 唯一的研究完成状态对象。 |

`brief`：`user_request` 保留用户原意及限制；`objective` 写用途和成功标准；`scope` 写本次对象、时间、地区、语言边界；三者均为非空字符串。`as_of` 为研究截止日期 `YYYY-MM-DD`，不是“已经搜索到该日期所有内容”的保证。`depth` 为 `quick / standard / deep`；`expansion_policy` 为 `off / adaptive / wide`；`assumptions` 为非空字符串组成的数组，可为空数组，不允许重复值。

## 3. 问题 questions

每项：`id`、`question`、`tier`、`acceptance`、`status`、`claim_ids`、`gap`。

- `id`：`Q` 加至少三位数字，例如 `Q001`。同组唯一，不要求编号连续。
- `question` / `acceptance`：非空字符串。分别写待解问题和本次用途下何种证据算够用。
- `tier`：`core / prerequisite / extension`。必要前提不是可选增益。
- `status`：`answered / partial / unanswered`。表示问题回答程度，不是自动计算的事实可信度。
- `claim_ids`：关联 C 编号数组。每个 C 的 `question_ids` 必须反向包含该 Q。问题已回答时不能为空，也不能全部依赖 `unverified` 结论。
- `gap`：未完全回答时必须说明缺口及影响；已回答时可以为空字符串。

这种双向引用只用于阻止孤立或错误关联，不是两份结论。调整问题关联时同步更新两个编号列表；结论正文仍只在 C 中存一份。

## 4. 来源 sources

每项：`id`、`title`、`locator`、`source_type`、`publisher`、`published_at`、`accessed_at`、`access_status`、`origin_group`、`reading_note`、`context`。

- `id`：S 编号。`title` 为真实标题或清楚的文件标识；`locator` 是稳定网址、DOI、用户文件路径/标识或可恢复的内部定位。不得为看似完整而编造 URL。
- `source_type` / `publisher`：描述资料种类与责任主体；不是高低等级。如果无法确认，填“未知，未核实”等明确说明。
- `published_at`：有把握的发表日期，未知则 `null`，不要推测月日。`accessed_at` 是实际查看日期。日期格式均为 `YYYY-MM-DD`。
- `access_status`：`full` 全文；`partial` 已读相关部分；`abstract` 仅摘要；`snippet` 仅搜索片段；`unavailable` 未读到。相关局部读完不等于全文读完。
- `origin_group`：声明共同原始证据的组标识，例如 `origin-pressrelease-2026-01`。转载同稿共享组。未知可以写 `unknown-S001`，并在 context 说明独立性未证实；不同字符串本身不证明独立。
- `reading_note`：具体读到的章节、页码、段落或片段与未读取部分。
- `context`：与问题有关的版本、地区、样本、方法、利益关系及限制，不以“可信”二字代替。

除 nullable 日期外，以上文本字段均非空。搜索到但未读到的来源可以保留为线索，不能偷偷升级为已核实证据。

## 5. 结论 claims 与支持关系 evidence

每项：`id`、`statement`、`question_ids`、`kind`、`status`、`confidence`、`confidence_reason`、`evidence`、`limitations`。

- `id`：C 编号。`statement` 是范围明确、可检查的陈述，不把多个互不相干判断揉成一句。
- `question_ids`：至少一个真实 Q 编号，且各 Q 反向引用本 C。
- `kind`：`fact` 事实；`inference` 分析推断；`recommendation` 建议；`hypothesis` 待验证假设。
- `status`：`supported` 当前陈述获得相符支持；`qualified` 只能在限制下成立；`contested` 存在未消解的支持与反证；`unverified` 尚未核实。
- `confidence`：`strong / moderate / weak / unknown`，是有理由的定性判断，不是概率。`confidence_reason` 必须非空，说明证据与限制，不能只重复枚举值。
- `evidence`：证据关系数组，结构见下表。
- `limitations`：一般必须非空；仅 `supported` 的 `fact` 可为空。分析和建议必须说明适用边界。

| evidence 字段 | 规则 |
|---|---|
| source_id | 真实存在的 S 编号。 |
| relation | `supports / contradicts / context`。 |
| locator | 在该来源中的实际页码、时间码、表格、段落或章节定位，非空。 |
| note | 说明来源的哪部分支持或限制当前陈述，非空；不是长篇复制原文。 |
| entailment | `direct / partial / none`。表示该材料与当前陈述的支持/反驳程度，而非抽象“权威性”。 |

`context` 必须配 `none`；支持/反驳配 `direct` 或 `partial`。同一结论下完全相同的 source_id、relation、locator 不重复登记。

结构门禁：事实/推断若声称 `supported / qualified / contested`，须有实际可读的支持来源。`supported` 还须有至少一处 `full / partial` 来源的直接支持；纯摘要只能降为 `qualified` 等合适状态，并保留全文未核实的限制。推断的证据还需人工核对推理是否超出前提，脚本不证明逻辑有效。

`contested` 需要可读支持与反证；仍有未消解反证时不能同时标 `supported`。已经因版本/口径不同被消解的材料可列为 `context`，在 note 说明为何不构成当前陈述的反证，不得为了过检任意降级。

`unverified` 只能配 `weak / unknown`；假设不能同时标 `supported`，已证实结果应重新分类。纯建议可以没有外部 evidence，但建议中的外部事实必须拆为单独有证据的事实项；不能利用 `recommendation` 绕过核实。摘要-only 不得配 strong；多个来源同 origin_group 会收到重复出处警告。

## 6. 延展 extensions

每项：`id`、`question_id`、`anchor_question_ids`、`why_relevant`、`benefit`、`status`。

- `id`：X 编号；`question_id` 对应一个 `tier=extension` 的 Q，且每个延展 Q 恰好有一个 X 路由。
- `anchor_question_ids`：至少一个 core/prerequisite Q；不允许只锚定另一延展，防止逐级越走越远。
- `why_relevant`：说明具体关联。`benefit`：说明对理解、判断或行动的收益。均非空。
- `status`：`include` 纳入输出；`defer` 保留待查；`reject` 本次排除。

include 需要关联问题已有结论或明确标注的建议；off 禁止 include 的可选延展。必要前提不受“不要拓展”剥离，但仍需简明说明其必要性。

若延展被证实是核心答案不可缺的前提：把 Q 提升为 `prerequisite`，移除其 X 路由，更新 brief.scope 并在报告说明范围变更。不要同时保留“可选延展”和“必答前提”两个身份。defer/reject 项的 Q 可保持 unanswered 并记录 gap；它们不会阻止核心研究 complete_for_scope。

## 7. 查询 queries 与素材 assets

`queries` 每项：`id`（R 编号）、`query`、`question_ids`、`channel`、`purpose`、`outcome`、`source_ids`。只记录实际执行的检索；`query` 可记录用户资料/站内查询文本，敏感内容脱敏。question_ids 至少一个，source_ids 可为空。其余均非空文本。待执行查询放报告“下一步”，不能作为已运行的 R 项。

`assets` 每项：`id`（A 编号）、`source_id`、`local_path`、`kind`、`inspection`、`inspection_note`、`sha256`、`rights_note`。

- 路径必须是相对记录目录的 POSIX 路径，如 `assets/frame-001.png`。不接受绝对路径、`..`、反斜线、冒号或空字符。脚本指定 `--root` 时改以该目录为根。
- `kind`：`image / page_clip / video_frame / text`。`inspection`：`verified / unverified`。verified 仅能在实际查看内容后填写，脚本不会替你看图。
- `inspection_note`：实际内容与检查范围，不把登录页/空白截图当正文。`rights_note`：允许的使用或未确认的版权限制；下载成功不是使用授权。
- `sha256`：已计算的 64 位小写十六进制摘要，或 `null`。有哈希时脚本比对文件；不提供哈希时不要求为了模板虚构。
- 所有文本字段非空。无下载需求时 assets 为空，不必落盘所有来源。

## 8. 完成状态、错误与检查边界

`completion`：`status` 为 `draft / complete_for_scope / partial / blocked`，`reason` 必须解释当前状态和范围。complete_for_scope 至少有一个核心问题，且所有核心和必要前提均 answered；增益延展不要求全部完成。partial/blocked 是合法结果，不代表应继续无休止搜索。

执行 `python scripts/validate_research.py <record.json>`：退出码 0 表示无结构错误，1 表示结构或内部一致性失败，2 表示文件/JSON/命令行输入失败。警告不会伪装成错误，也不自动改变事实状态。

脚本只读文件；校验字段、编号引用、声明状态及可选素材路径/哈希。不会联网、判断文字的真实支持关系、验证真实来源独立性、确认图片实际看过、授予版权或判断研究是否充分。**校验通过 ≠ 调研正确，也不等于整个技能行为验收通过。**

# 正式文件交付的最小状态合同

## 职责分开，但不维护多份真相

- **正文权威**：`project.json.current.file` 指向的标准剧本；内容只写在该文件。
- **选择与批准权威**：`project.json` 指明哪份正文是当前稿、用户批准绑定哪份快照、哪份提示词是它的派生。
- **派生视图**：提示词版和逐场对照；不得反向覆盖标准稿。

本约定是当前 Skill 的操作合同，不沿用原研究接口中 `proposal/current/consumed/checked` 作为另一套生产状态。那些术语可用于研究解释，但不得再平行维护当前批准。

## 文件约定

```text
project.json
screenplay-v001.md
screenplay-v001-prompts.md       # 确认后才成为正式派生稿
alignment-v001.md               # 双版本文本对照，不是第三份剧本
```

未来有 v002 就新增文件，不覆盖 v001。普通聊天阶段可以只用可辨认的版本条；跨会话或正式文件交付才使用本合同。用户主要接收两份剧本；JSON 和对照文件作为配套交接依据，可放支持资料目录或一并提供。

## 字段和消费者

顶层只允许 `schema_version`、`project_id`、`current`、`approval`、`derived`。省略的可选对象用 null，不创建多重状态字段。

| 字段 | 谁使用、如何使用 |
|---|---|
| `schema_version: 1` | 校验器选择本格式，不猜未知版本 |
| `project_id` | 使用者辨别项目；跨项目不能套用批准 |
| `current.version/file/sha256` | 写作、转译、交付者都先读取该文件并核对 SHA-256；不择最新文件 |
| `approval.version/sha256` | 仅与 current 完全匹配才视为对应快照获批 |
| `approval.quote/context` | 保存实际用户确认原句与可复查语境；人工/Agent 核验语义与身份，脚本只能检查非空 |
| `derived.file/sha256` | 下游定位实际提示词文件并核对字节 |
| `derived.source_version/source_sha256` | 防止旧提示词挂到新稿；必须匹配 current |
| `derived.alignment_file/alignment_sha256` | 对照者读取实际审查记录；交付者核对其身份；记录哈希不等于审查结论正确 |

模板中的 `approval` 和 `derived` 永远为 null。禁止从 examples/evals 拷贝示例批准充当真实记录。

## 推导状态与下一动作

| 实际条件 | 推导状态 | 下一动作 |
|---|---|---|
| 当前稿有效，approval 为 null，derived 为 null | 候选稿 | 继续修改或请求最终确认 |
| 有效批准，derived 为 null | 标准稿已确认，转译未完成 | 读取该稿并完成同源 B 与对照 |
| 批准、两文件、来源关系、对照记录均一致 | 配对文件在结构上相符 | 完成人工/Agent语义对照后交付，并标媒体未测 |
| 哈希/版本/场次/确切文本不一致 | 文件冲突，不是完成 | 定位哪层失配，修复或回到候选 |

不单独保存 `status`、`is_final`、`next_action` 等重复字段，避免正文、批准和状态互相打架。下游不得只读取派生稿文件名就继续；必须先核对 project 的 current、批准和 derived 来源。

## 状态更新纪律

新稿产生后：写新正文 → 算哈希 → 将 current 指向它 → 将当前 approval/derived 设 null。旧文件可归档，旧批准不是新版批准。最终确认后：引用真实确认 → 匹配当前快照 → 保存 approval → 从同一稿派生 B → 完成对照 → 记录 derived。不能先写“已批准”，再打算请用户确认。

有修改时不要覆盖已确认文件；否则应如实报告冲突，不更新批准哈希掩盖变更。需要归档批准记录可保存历史只读副本，但运行只消费 current 指针，历史不自动复活。

## 校验命令与边界

在项目文件夹之外可使用安装目录中脚本的绝对路径：

```bash
python /path/to/screenplay-writing-iteration/scripts/check_delivery.py --hash screenplay-v001.md
python /path/to/screenplay-writing-iteration/scripts/check_delivery.py project.json
python /path/to/screenplay-writing-iteration/scripts/check_delivery.py project.json --require-final
```

脚本只读，使用 Python 标准库；相对项目文件路径解析于 `project.json` 所在文件夹。它检查字段、引用文件、哈希、批准/来源绑定、场次顺序和带 ID 的精确对白/旁白/屏幕文字。`--require-final` 要求具备配对交付，尚处草稿时返回未满足。

**脚本不认证用户身份/自然语言确认，不理解剧情，不判断艺术质量，也不证明生成效果。** 必须实际阅读逐场对照与用户确认；未运行就写未运行。聊天环境无 Python 时按同等合同手工检查，不凭空编造哈希或“程序通过”。

对照文件头须包含 `标准稿版本：v001` 与 `标准稿 SHA-256：实际哈希`，防止记录挂错源。记录未做的媒体、受众、参数执行验证，不写“全链路已验证”。

# 剧本创作润色与双版本定稿

版本：1.0.0 · 构建日期：2026-09-18

从需求或现有稿写作、润色和多轮迭代，确认后给标准剧本与同源提示词描述版。

## 使用

解压后保留整个 `screenplay-writing-iteration/` 目录，不要只拿 `SKILL.md`。本地 Codex 项目可放到 `.agents/skills/screenplay-writing-iteration/`；个人级可放到 `~/.agents/skills/screenplay-writing-iteration/`。不要在同一范围重复安装相同名称。

在支持独立 Skill 的宿主中加载此文件夹。ChatGPT 可通过 `@` 选择技能；Codex 可用 `$screenplay-writing-iteration` 显式调用。不同宿主的导入入口与管理员权限可能不同；本 ZIP 是技能文件夹交付，不表示已在你的应用安装，也不保证任意网页聊天支持直接上传 ZIP 安装。

官方结构/加载依据与核验日期见 [来源说明](references/source-notes.md)。不需要绑定第三方生成服务或购买 API；文本工作以指令为主。可选检查脚本需要 Python 3.9 或更新版本，只使用标准库、只读文件。

## 目录

- `SKILL.md`：唯一运行入口，定义触发、边界、步骤与交付。
- `agents/openai.yaml`：中文界面名称及调用提示。
- `references/`：可执行规程、按问题路由与 303 份原知识资料的可移植副本。
- `assets/`：本技能的输出模板，不是预填的真实结果。
- `examples/`：自拟输入与示范，学习处理边界与输出，不代表生成实验。
- `evals/`、`tests/`、`scripts/`：行为用例与静态检查工具；运行范围见 [验证报告](VALIDATION.md)。

正文知识按需读取，不要求每次填完全部表格。原包引用但未提供的历史文件已注明，不会伪装成本次可读来源。

## 最快的调用方式

```text
请使用 $screenplay-writing-iteration，根据以下需求或附件原稿写作/润色。按我的反馈持续改稿，不要擅自改掉锁定内容；我明确确认最终版后，再给标准剧本和同一版本的当代提示词描述优化版。
```

## 运行与验证边界

“不错、继续”不是自动定稿；批准绑定具体正文。提示词转译不能改变主动权、揭示时机、台词、道具去向或结局。

检查脚本通过只证明明列的静态条件；模型实际触发、长对话行为、语义判断、真实媒体与受众效果没有因此得到认证。请按 [行为评测](evals/README.md) 在实际宿主检验。

## 本地复查

在本目录运行：

```bash
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v
python scripts/check_package.py .
```

第一行避免产生 `__pycache__` 打包杂项；Windows 可先设置同名环境变量。文件创建后的修改会改变校验结果，知识源文件的更新须同步维护来源清单。

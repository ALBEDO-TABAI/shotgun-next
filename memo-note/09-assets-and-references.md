# 09 · 可复用资产与外部参考

最后更新：R2（2026-09-17）
本轮变化：新建。

## A. skill 包（直接复用）

路径：`/Users/bai/实验田/idea-3/skills/new-version/`

| 资产 | 路径 | 在 shotgun 中的用途 |
|---|---|---|
| bundle 清单 | `bundle-manifest.json` | skill 加载器的入口列表（9 个 skill、入口路径与字节数） |
| 导演 skill 入口与路由表 | `director-skill/vvf-director-skill/SKILL.md` | 导演节点、编译节点、审片节点的加载依据 |
| 任务分流 / 最小需求记录 | `.../references/brief-and-modes.md` | 第一张纸之前的需求澄清骨架 |
| 交接字段与上下文胶囊 | `.../references/collaboration-and-revision.md` | 05 的 Artifact 字段来源；hold 时写盘的胶囊格式；多岗逐镜审稿表 |
| 提示词编译 | `.../references/prompt-compilation.md` | 编译节点方法 |
| 生成审片 | `.../references/generation-review.md` | 审片节点方法；Take 结论格式 |
| 生成单元骨架 | `.../assets/video-prompt-skeleton.txt` | GenerationUnit 的文本格式 |
| 结构校验脚本 | `.../scripts/validate_prompt.py` | fire 门；参数 `--max-chars / --per-shot / --max-handles` 从 provider 能力表注入 |
| 三本台账 CSV | `addon/vvf-script-supervisor/assets/*.csv` | 05 的 GenerationUnit / Take / 连续性 schema 来源 |
| 项目风格档案 | `addon/vvf-script-supervisor/assets/project-style-profile.json` | StyleProfile 实体 |
| 8 个 addon skill | `addon/vvf-*/SKILL.md` | 各工种节点 |
| 结构校验器 | 上级目录 `tools/validate_bundle.py`（需 PyYAML、markdown-it-py） | CI 里校验 skill 包结构 |

## B. 旧 dossier 里值得借的机制（D-11：仅参考）

路径：`/Users/bai/实验田/shotgun-next/shotgun/`、`docs/`、`modules/`

| 机制 | 出处 | 借用方式 |
|---|---|---|
| "文件出现"不等于"完成"：dispatch 必须以 reply(+outcome) 收口 | 00-brief §5、M06 | 节点的 passed 必须由确认需求工具的 yes + 工件 ready 触发，不是文件写入 |
| 占位符即阻塞（TBD、空帧、lorem） | 00-brief §5 | critic / validate 时把占位符当 P0 |
| variants 而非 revisions（D8） | 09-decisions | Take 是 variant |
| style lock 作为一等实体（D7） | 09-decisions | 用 project-style-profile.json 实现 |
| 静态前缀 / 易变尾部的提示拆分 | 05-prompt-system | 每个节点的 developer instructions 保持字节稳定以利缓存 |
| 每个工具结果附 `next` 提示 | 09-decisions D15 | dynamicTools 的返回值里带下一步建议 |
| 导入的知识不可信，需 diff 审阅 | D14 | 用户往 skill 目录投放新 skill 时先看 diff |
| 生成前 `cost_estimate` 门 | 08-build-plan 风险表 | 制片 HUD 的 fire 前估算 |

不借：wake engine、autonomy lanes、OKR 状态机、3D floor、marketplace、receivable。

## C. 外部调研（2026-09-17）

| 项目 | 链接 | 备注 |
|---|---|---|
| Codex app-server README | https://github.com/openai/codex/blob/main/codex-rs/app-server/README.md | 方法清单、dynamicTools、thread/fork、requestUserInput |
| Codex SDK（TS） | https://github.com/openai/codex/tree/main/sdk/typescript | `@openai/codex-sdk` |
| Codex 子 agent 文档 | https://developers.openai.com/codex/subagents | 了解其内部子 agent 模型，shotgun 不直接用 |
| Codex skills 文档 | https://developers.openai.com/codex/skills | SKILL.md 标准与 `.agents/skills` 发现路径 |
| HyperFrames | https://github.com/heygen-com/hyperframes | Apache-2.0；studio / player / producer / shader-transitions |
| Remotion 许可 | https://www.remotion.dev/docs/license/faq | ≤3 人免费；Automators $0.01/render、$100/月起；Editor Starter 仅 Enterprise |
| Twick | https://github.com/ncounterspecialist/twick | MIT React 编辑 SDK |
| AiCut | https://github.com/ipmotionmc/AiCut | MIT，可嵌入组件 |
| Elah | https://github.com/elahlabs/elah | WebGL2 + WebCodecs 引擎 |
| Diffusion Studio Core | https://github.com/diffusionstudio/core | 免费带水印 |
| OpenCut（UnderHear） | https://github.com/UnderHear/OpenCut | "LibTV 同款"时间线组件 |
| @chatoctopus/timeline | https://github.com/ChatOctopus/timeline | FCPXML / xmeml / OTIO 导入导出 |

## D. 用户本机相关

- `codex-cli 0.145.0` 已安装（`/opt/homebrew/bin/codex`）。
- 用户有 Tauri（hfp-allinone-tauri）与 Electron（ready-cowork）项目经验；有 libtv-cli skill（与 OpenCut "LibTV 同款"可能相关）。

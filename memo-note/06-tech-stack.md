# 06 · 技术基座与选型

最后更新：R2（2026-09-17）
本轮变化：新建。完成 codex app-server、剪辑引擎（hyperframes / remotion / twick / AiCut / elah / diffusion studio / OpenCut）、互换格式（OTIO / FCPXML / xmeml）的首轮调研。平台未定。

所有 **[调研]** 内容带日期 2026-09-17；版本号与价格是当期参数，实施前需再核。

## A. agent 运行时：codex app-server 作为基座

**[用户 R2-4]** codex harness 开源，似乎可作为基座；具体实现未想好。

**[调研 2026-09-17]**

- 本机已装 `codex-cli 0.145.0`；`~/Projects/codex` 目录不存在（用户 codex-debugging skill 里提到过，可能已移走）。
- `codex app-server` 是 Codex VS Code 扩展等富客户端所用的接口，Rust crate `codex-rs/app-server`，开源。JSON-RPC 2.0 双向通信；传输：`--stdio`（JSONL，子进程嵌入的一等路径，v0.136+）、unix socket、websocket（实验）。
- `codex app-server generate-ts` / `generate-json-schema` 可导出与本版本完全匹配的 TS 类型 / JSON Schema。
- 三层模型：Thread（线程）→ Turn（轮）→ Item（项）。
- TypeScript SDK `@openai/codex-sdk` 内部也是 spawn `codex app-server --stdio`；提供 `startThread / run / runStreamed / resumeThread`、结构化输出 schema、`env` 控制（文档特别提到适合 Electron 等沙箱宿主）、`skipGitRepoCheck`。

**与 shotgun 需求的映射 [建议]**

| shotgun 需求 | app-server 能力 | 备注 |
|---|---|---|
| 每个节点一个子 agent 会话 | 一个节点 = 一个 `thread`；`thread/start` 指定 `cwd`（节点目录）、model、approval、sandbox / permissions | 由 shotgun 自己编排节点间关系，不用 codex 内部的 Multi-Agent V2（父线程拥有的子 agent 拒绝直接 turn，不适合"每个节点给用户聊天入口"） |
| 加载工种 skill | `skills/extraRoots/set`（进程级、不持久化）+ `skills/list`；或 cwd 下 `.agents/skills` | skill 的 SKILL.md 格式与 codex agent skills 标准一致（name / description 前置） |
| 确认需求工具 | `dynamicTools`（`thread/start` 时注册；需 `initialize.capabilities.experimentalApi = true`）→ agent 调用时服务端向客户端发 `item/tool/call`，客户端渲染卡片并回传结果 | 备选：内置 `item/tool/requestUserInput`（1–3 个短问题，实验） |
| 工件提交 / 成本上报等应用侧工具 | 同上 dynamicTools，或以 MCP server 形式挂给 codex | dynamicTools 更直接，MCP 更可移植 |
| branch | `thread/fork`（可 `lastTurnId` 截断、`ephemeral`），返回 `forkedFromId` | 与 03 的分支语义直接对应 |
| refresh-overwrite | 同 thread 新 turn + 工件新 revision；或 `thread/revert`（`beforeTurnId`） | `thread/rollback` 已标 deprecated，不要用 |
| hold / 恢复 | `thread/resume`；线程持久化在 `~/.codex/sessions` | 上下文胶囊仍建议自己写盘 |
| 制片 HUD 的 token 成本 | `thread/tokenUsage/updated` 通知 | 生成调用成本由 shotgun 自记 |
| 审批 | `item/commandExecution/requestApproval`、`item/fileChange/requestApproval` | 节点 agent 主要写 Markdown 工件，可用宽松策略 |
| 结构化输出 | SDK `outputSchema`；app-server 对应 turn 选项 | 用于让 agent 直接产出 GenerationUnit JSON |
| 线程命名 / 目标 | `thread/name/set`、`thread/goal/set` | 目标 = 节点任务单 |

**需要注意的点 [建议]**

1. `dynamicTools`、`requestUserInput`、`permissions` 等标"experimental"，接口可能变；用 `generate-ts` 锁版本，升级时重新生成。
2. Codex 默认是编码 agent：系统提示偏代码、要求 cwd 是 git 仓库（可 `skipGitRepoCheck`）、有文件改动审批流。作为通用创作 agent 运行时可用，但要给每个节点写明确的 developer instructions（skill 加载 + 角色边界）。
3. 模型与账号：默认走 OpenAI（ChatGPT 订阅或 API key）。codex 的 `model_providers` 配置支持 OpenAI 兼容端点，但能力（工具调用、结构化输出、缓存）以实测为准。若要用非 OpenAI 模型做某些工种，要先验证。
4. 备选运行时：Claude Agent SDK；或自己在 Responses API 上写一个薄循环。前者对 skill 与子 agent 支持成熟，后者最可控但要自己做工具循环、会话持久化与审批。R2 阶段不做决定，见 Q-12。

## B. 客户端平台

**[用户 R2-7]** Electron / Tauri / Swift 未定；短期 Swift 也可接受。

**[分析 建议]**

| 维度 | Electron | Tauri | Swift (SwiftUI + AppKit) |
|---|---|---|---|
| 与 codex app-server 集成 | Node 直接 spawn，或用 `@openai/codex-sdk` | Rust 侧 spawn 子进程、转发 JSONL 到前端；或前端 sidecar | `Process` + `Pipe` 读 JSONL，用 `generate-json-schema` 生成 Codable |
| 液态玻璃 | CSS backdrop-filter 模拟；层数受限 | 同左 | macOS 26 原生 Liquid Glass 材质，免费且真实 |
| 剪辑 / 组装界面 | 直接嵌 React 组件（twick / hyperframes studio / AiCut） | 同左 | 需 WKWebView 嵌 Web 组件 → 变成混合应用；或用 AVFoundation 自写时间线（工作量大） |
| 渲染导出 | Node + ffmpeg 子进程 | Rust / sidecar + ffmpeg | `Process` + ffmpeg，或 AVFoundation 合成 |
| 跨平台 | 是 | 是 | 否（用户目标用户是工作室朋友，可能全 Mac） |
| 用户已有经验 | 有（ready-cowork） | 有（hfp-allinone-tauri） | 有 Swift 意愿 |
| 复杂动画（射线、霜层、纸展开） | Web 动画栈成熟（Motion / GSAP / WebGL） | 同左 | SwiftUI 动画 + Metal，质量高但迭代慢 |

**[建议]** 关键耦合点是**剪辑组装界面**：目前所有可复用的开源时间线组件都是 React。如果选 Swift，这一块要么 WKWebView 嵌入（混合），要么自写。若玻璃与原生手感是首要，Swift + WKWebView(剪辑) 是可行的混合路线；若迭代速度优先，Electron / Tauri 全 Web。R2 不决定，见 Q-13。

## C. 剪辑 / 组装引擎

**[用户 R2-7]** 查 hyperframe、remotion 等；基础剪辑 + 部分图形制作即可；专业调色导出工程给 PR / 达芬奇。

**[调研 2026-09-17]**

| 方案 | 性质 | 许可 | 时间线 UI | 导出 | 备注 |
|---|---|---|---|---|---|
| **HyperFrames**（heygen-com/hyperframes） | HTML/CSS + 媒体 + 可 seek 动画 → 确定性 MP4；Puppeteer 抓帧 + FFmpeg 编码 | Apache-2.0，无按次收费 | `@hyperframes/studio`（React：时间线、代码编辑器、预览、inspector） | MP4（自带 producer 管线，含音频混合） | 2026-03 创建，43k+ stars；`@hyperframes/player` 可嵌入；面向 agent（agent 写 HTML）；有 `npx skills add heygen-com/hyperframes` 的 agent skill；图形 / 字幕 / 转场（`shader-transitions`）能力强 |
| **Remotion** | React 组件 → 视频；Player + Editor Starter | 个人 / ≤3 人公司免费；≥4 人需 Company License：Automators $0.01/render、$100/月起；Editor Starter 仅 Enterprise（$500/月起） | Editor Starter（付费层） | MP4（服务端渲染） | 工作室人数决定是否触发许可；"prompt-to-video / 视频编辑器"明确属于 Automators |
| **Twick**（ncounterspecialist/twick） | React 视频编辑 SDK：`@twick/studio` 全套 UI、timeline、canvas、browser-render（WebCodecs）、render-server | MIT | 完整 studio | 浏览器 WebCodecs 或服务端 Puppeteer+FFmpeg | 含 MCP agent 包；浏览器导出仅 Chromium |
| **AiCut**（ipmotionmc/AiCut） | 框架无关 core + React/Vue 薄壳；Canvas 时间线；JSON 工程 | MIT | 有 | BYO 后端（提供 Fastify / Go 参考实现，ffmpeg + SSE 进度） | 小项目（4 stars），成熟度存疑 |
| **Elah**（elahlabs/elah） | 浏览器原生帧精确引擎：WebGL2 渲染、WebCodecs、整数帧时间 | 未在摘要中确认 | React 绑定 | 浏览器 MP4（mediabunny） | 架构描述扎实；成熟度待看 |
| **Diffusion Studio Core** | WebCodecs 合成引擎（类 Pixi 架构） | MPL-2.0 代码，但免费使用要保留水印，去水印买 license | 无（自建） | 浏览器 | 商业条款不利 |
| **OpenCut**（UnderHear/OpenCut，"LibTV 同款"） | 纯前端 React 时间线组件 | MIT | 有 | 不含编码器，导出 JSON 由宿主实现 | 用户可能认识 LibTV；另有更知名的 OpenCut-app/OpenCut（Next.js CapCut 替代），当前状态需核实 |

**互换格式 [调研 2026-09-17]**

- `@chatoctopus/timeline`（npm）：`exportTimeline(timeline, "fcpx" | "premiere" | "resolve" | "otio")`，生成 FCPXML 1.8 / xmeml v5 / OTIO，有理数时间无浮点漂移，不需要 ffmpeg；也能 `importTimeline`。
- 达芬奇 Resolve 18+ 原生读 OTIO；Premiere 读 xmeml v5（FCP7 XML），不读 OTIO；Final Cut 读 FCPXML。
- 工程文件只描述剪辑不带媒体；导出时要一起给出媒体目录并用相对路径或可重链的文件名。

**[建议] 初步方向（未定，见 Q-14）**

1. **组装层**用 ffmpeg 直接做：Take 拼接、in/out、简单 xfade、音乐轨混合。生成的素材是一段段视频，这是最简单、最可控、最快的路径。
2. **图形层**（标题、字幕、包装、转场）用 HyperFrames：agent 写 HTML 组合，确定性渲染；Apache-2.0 无许可风险；剪辑 skill 或独立"包装"节点可以直接产出 HyperFrames 组合。
3. **时间线 UI**：优先评估 `@hyperframes/studio`（若能只取时间线组件）和 Twick（MIT、完整）。Remotion 因 Editor Starter 锁在 Enterprise 且工作室人数可能触发许可，暂列备选。
4. **导出**：`@chatoctopus/timeline` 产 OTIO（给达芬奇）+ xmeml（给 PR），附媒体目录。

## D. 生成 provider

- **[用户 R2-8]** 只做生成。
- **[用户 R2-10]** 音乐：音乐生成服务；配音 / 音效：写进视频生成提示词。
- **[建议]** 需要一张 provider 能力与价格表（02 缺口清单）。字段：provider、模型、模式（文生视频 / 图生视频 / 首尾帧）、最大时长、分辨率、参考图数量与句柄语法、音频能力（是否生成对白 / 音效）、单价、`valid_as_of`。编译节点按此表填 `validate_prompt.py` 参数。
- **[建议]** 配音随视频生成的已知弱点：跨镜头声线一致性、口型、中文台词准确度因模型而异。先按用户方案做，但数据模型预留 TTS 轨，以便某些镜头改为独立配音。
- 具体 provider 名单与 API 权限未定，见 Q-15。

## 待定

- Q-12 运行时最终选择（codex app-server / Claude Agent SDK / 自写）。
- Q-13 客户端平台。
- Q-14 剪辑引擎组合。
- Q-15 生成 provider 名单与权限。

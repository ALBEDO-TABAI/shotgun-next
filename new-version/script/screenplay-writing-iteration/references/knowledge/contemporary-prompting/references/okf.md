---
type: Reference
title: OKF 封装说明
description: 这个知识包按 OKF v0.1 组织。哪些是规范要求、哪些是这本书自己的约定、怎么校验和更新。
tags:
- OKF
- 维护
- 格式
- skill
timestamp: '2026-09-18'
source:
- 用户上传：okf-bundle-ready.zip
- Open Knowledge Format 公开规范
---
> 本次封装注：以下为用户提供知识包的存档内容。原文提到的旧 Skill、阅读器、截图、研究原文或安装状态，不表示它们随本包存在或已经运行；本次实际入口为外层 `SKILL.md`。历史接口仅供研究，不覆盖外层工作规则。


# OKF 封装说明

## 用的哪个版本

用户上传的 `okf-bundle-ready.zip` 明确要求按 OKF v0.1 组织，并运行随附的校验器。这次以此为兼容目标，不擅自升级。

核验到的公开 OKF 仓库已迁移，当前公开规范包含 v0.2。这里不宣称兼容目标是最新版本。[1][2]

## 哪些是规范，哪些是这本书的选择

**规范要求**：每个概念 Markdown 有 YAML frontmatter 和非空 `type`；包根 `index.md` 只声明 `okf_version: "0.1"`；子目录索引不带 frontmatter；`log.md` 按日期记录。

**这本书的选择**：来源放在 `# Citations`，用包根相对 Markdown 链接关联概念。`title`、`description`、`tags`、`timestamp` 是为了方便阅读和检索；`source` 是本地扩展，不是规范必填。概念 ID 由文件路径得到，没有伪造 ID 体系。

**本地 type 词表**：

| type | 意思 |
| --- | --- |
| `Framework` | 框架 |
| `Technique` | 技巧 |
| `Lexicon` | 图谱 |
| `Playbook` | 流程与工具 |
| `CaseStudy` | 案例 |
| `Exercise` | 练习 |
| `Reference` | 来源 |

这是本包约定，不是全局标准。

## 谁是内容源

`knowledge/contemporary-prompting/` 里的 Markdown 是**可编辑的内容源**。`开始阅读.html` 由这些文件生成，是离线阅读副本。**不要只改 HTML 就说知识库已更新。**

`OKF-INDEX.md` 是本地交付工作区的登记索引，不是知识包内的规范文件。

附带的 skill 在 `skills/contemporary-prompt-expert/`，是自包含的：`SKILL.md` + `references/` + `examples/`，内部全部用相对链接。它只导航知识，没有自动执行、联网或生成权限。

## 校验与更新

在交付根目录运行：

```bash
python scripts/okf_tools.py validate knowledge/contemporary-prompting --verbose
python scripts/build_reader.py
python scripts/verify.py
```

刷新工作区索引：

```bash
python scripts/refresh_index.py
```

读 HTML 和 Markdown 不需要装依赖。重建和校验需要的 Python 包列在根目录 `requirements.txt`。脚本不调用生成服务、不联网、不改来源 ZIP。

用户提供的原校验器以绝对路径保存索引条目。本包附的 `refresh_index.py` 会把本包登记迁到解压后的实际位置，避免因目录移动出现旧条目。这是交付辅助，不是 OKF 规范。

## 需要使用者自己确认的

六个问题和图谱适不适合你的项目类型，需要实作；情绪词的具体读法需要目标语境；工具接口和音频标签需要在实际调用前核对。**文件格式检查不能替代这些。**

v0.2 用了不同的来源和生成元数据字段。将来迁移应按公开规范映射，不直接改版本号。当前包保留 v0.1，让你上传的 skill 可以继续验证。[2]

# Citations

[1] 用户上传 `okf-bundle-ready.zip` 内：`SKILL.md`、`references/okf-spec.md`、`references/templates.md`、`scripts/okf_tools.py`。

[2] [Open Knowledge Format — 当前公开 SPEC 及 v0.1 迁移说明](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md)

[3] [原 knowledge-catalog/okf 仓库的迁移说明](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/README.md)

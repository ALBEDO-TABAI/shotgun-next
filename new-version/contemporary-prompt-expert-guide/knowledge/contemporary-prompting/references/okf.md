---
type: Reference
title: 封装与维护：按上传skill的OKF v0.1交付
description: 说明知识包、派生阅读器、校验器与索引的各自职责，不混同规范与团队约定。
tags:
- OKF
- 维护
- 格式
- skill
timestamp: '2026-09-18'
source:
- 用户上传：okf-bundle-ready.zip
- Open Knowledge Format公开规范
---

# 封装与维护：按上传skill的OKF v0.1交付

## 本包采用哪个版本

用户上传的`okf-bundle-ready.zip`明确要求按OKF v0.1组织并运行随附校验器。本次以此作为兼容目标，不擅自升级。核验到的公开OKF仓库已迁移，当前公开规范包含v0.2；这里不宣称兼容目标就是最新版本。[1][2]

## 哪些是规范，哪些是本书的选择

每个概念Markdown有YAML frontmatter与非空`type`。包根`index.md`只声明`okf_version: "0.1"`；子目录索引不带frontmatter；`log.md`按日期记录。本书的来源放在`# Citations`，并用包根相对Markdown链接关联概念。

`title`、`description`、`tags`、`timestamp`为便于阅读与检索的字段；`source`是本地来源扩展，不是规范必填。概念ID由文件路径得到，没有伪造必填ID体系。

本地type词表：`Framework`为框架；`Technique`为技巧；`Lexicon`为图谱；`Playbook`为流程与工具；`CaseStudy`为案例；`Exercise`为练习；`Reference`为来源。它们是本包约定，不是全局标准。

## 谁是内容源

`knowledge/contemporary-prompting/`中的Markdown是可编辑内容源；`开始阅读.html`由这些文件生成，是离线阅读副本。不要只改HTML后宣称知识库已更新。

`OKF-INDEX.md`是本地交付工作区的登记索引，不是知识包内的规范文件，也没有写入用户的GitHub或持久Library。附带消费skill只导航知识，没有自动执行、联网或生成权限。

## 校验与更新

在交付根目录中，可运行：

```bash
python scripts/okf_tools.py validate knowledge/contemporary-prompting --verbose
python scripts/build_reader.py
python scripts/verify.py
```

需要刷新工作区索引时运行：

```bash
python scripts/refresh_index.py
```

阅读HTML与Markdown不需安装依赖；重建和校验所需Python包列在根目录`requirements.txt`。脚本不调用生成服务，不联网，也不改来源ZIP。

用户提供的原校验器以绝对路径保存索引条目。本包附的`refresh_index.py`会把本包登记迁到解压后的实际位置，避免因目录移动出现旧条目；这属于交付辅助，不是OKF规范。

## 需要使用者确认的高价值项

六层框架和图谱是否适合你的项目类型，需要实作；情绪词的具体读法需要目标语境；工具接口与音频标签需要在实际调用前核对。这些不以文件格式检查替代。

v0.2采用不同的来源与生成元数据字段；未来迁移应按公开规范映射，不直接改一个版本号。当前包保留v0.1，使你上传的skill可以继续验证。[2]

# Citations

[1] 用户上传`okf-bundle-ready.zip`内：`SKILL.md`、`references/okf-spec.md`、`references/templates.md`、`scripts/okf_tools.py`。

[2] [Open Knowledge Format — 当前公开SPEC及v0.1迁移说明](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md)

[3] [原knowledge-catalog/okf仓库的迁移说明](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/README.md)

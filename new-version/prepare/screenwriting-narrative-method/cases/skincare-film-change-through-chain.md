---
type: Case Study
title: "护肤片案例：一个改动如何穿过全链"
description: 自拟案例。剪辑删除发送确认画面后，界面、表演、声音与字幕互相冲突；示范修复步骤、两条可选路线与一份变更记录，并说明不需要的过度方案。
tags: [topic-12, 护肤片, 变更记录, 部门冲突]
timestamp: 2026-09-18T00:00:00Z
source: new-version/script/12_创作迭代验证与协作交付流程.md#十二、以护肤片为例：一个改动如何穿过全链
---

# 案例（自拟）

原决定：她发出"我明早看"。它依赖四个条件：请求可延期、草稿未发送、最终句已发送、恢复护理的行动。

## 冲突是怎样产生的

剪辑为了加快节奏删除了发送后的确认画面。结果：

| 通道 | 状态 |
|---|---|
| 界面 | 仍有未发光标 |
| 表演 | 演员在镜中看了一眼，像在等待 |
| 声音 | 用了发送提示 |
| 字幕／说明 | 写成已经回应 |

这是请求、画面、声音与描述互相冲突，不是加一句"总体正确"可以解决的。

## 修复步骤

1. 先确定当前选择究竟是**已回应**还是**暂放**。
2. 若保留已回应：修界面和镜头使事实清楚；同步声音、字幕与场景记录；重新检查读取时间和动作连接。
3. 若改为暂放：更新任务范围，不能继续宣称完成了明确协商。
4. 两条路线都可以讨论，但不能让各部门保留自己喜欢的版本。

## 不需要的过度方案

不必为此创建庞大的自动规则引擎、让五个 Agent 重复判定，也不必修改全部人物资料。一个清楚的变更记录加实际样稿检查可能足够。

## 变更记录示例

```yaml
change_id: CH-SKIN-04
from_version: A-01
to_version: A-02
issue: 画面未确认发送，与声音和说明冲突
decision: 保留明确回应
changed: [界面状态, 镜头出口, 声音时点]
unchanged: [可延期前提, 产品不引发人格转变]
consumers: [界面制作, 剪辑, 声音, 字幕]
verification: 实际样稿能辨认最终消息已发送
status: 变更示例，尚未执行
```

# 适用边界

- 本案例为自拟，状态字段本身注明"尚未执行"；不是真实品牌方案或验证结果。

# 关系

- 上位主题：[本篇枢纽](/topics/12-iteration-and-handoff.md)；案例母体见 [护肤片案例枢纽](/topics/10-skincare-film-case.md)。
- 被破坏的是 [五个关键关系](/cases/skincare-film-five-protected-relations.md) 之一；类似的对抗性修改见 [五种对抗性修改](/cases/skincare-film-adversarial-modifications.md)。
- 修复遵循 [阶段G](/methods/stage-g-production-protection.md) 的"变更回到影响层级"，变更记录对应 [最小协作架构](/frameworks/minimal-collaboration-architecture.md) 的第三类文件与 [决策记录](/templates/decision-record.md)。
- 手机文字的事件状态（草稿／已发送）见 [旁白、字幕与手机文字](/frameworks/voiceover-captions-and-phone-text.md)。

# Citations
[1] [12 创作迭代验证与协作交付流程 §十二](../../../12_创作迭代验证与协作交付流程.md)

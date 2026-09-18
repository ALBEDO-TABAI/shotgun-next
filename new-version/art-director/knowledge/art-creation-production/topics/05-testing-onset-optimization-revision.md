---
type: Topic Guide
title: "05 测试、现场优化与回修：从“这版不够好”到定位、改变、验证"
description: "建立可在样片、工坊、棚内、场地和数字制作中使用的试验与回修方法：四种测试、基准、色彩链路、单变量与组合试验、区组与重复、四种判定、诊断树、故障表、回归、验收边界、反馈与停止条件。"
tags: [topic-05, 主题枢纽]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/art-director/美术创作与制作知识包_v2/05_测试现场优化与回修.md#05_测试现场优化与回修"
---

# 本篇概览

本篇任务：不是把审美变成总分，而是使每一次试做减少一项真实的不确定。

**主线：** [四种测试：探索／诊断／适用性／运行——不共用一个“通过”](/frameworks/four-test-types.md) → [哪个试验先做：看后果、牵连与可逆性](/methods/test-priority-ordering.md) → [把问题写成能被证据回答的句子：对象、条件、改变、观察、决策](/methods/testable-question-sentence.md) → [建立基准：六组条件的最少记录](/templates/test-baseline-record.md) → [四格组合试验：把材料与光放在一起比较](/methods/two-by-two-factorial-test.md) → [试验判定的四种结果：满足当前条件／局部可用／不满足／证据不足](/frameworks/four-test-verdicts.md) → 现场诊断树 → [修改后的回归检查：只复查受影响的链，不全案重审](/methods/regression-check-affected-chain.md) → [从试拍到可用：验收应覆盖的五种边界](/frameworks/acceptance-boundaries.md) → [何时停止测试：把资源留给仍有价值的问题](/principles/when-to-stop-testing.md)。

**内容身份：** 文中试验表和假设故障是应用方法；未开展实体试验，不填造结果。

# 本篇概念

## 框架 · Framework

* [从试拍到可用：验收应覆盖的五种边界](/frameworks/acceptance-boundaries.md) - 观看边界、时间边界、操作边界、处理边界、专业边界；一个角度通过不代表其他角度，开头结尾截图不代表中间状态，画面验收不替代安全；艺术目标与运行目标分列。
* [四种测试：探索／诊断／适用性／运行——不共用一个“通过”](/frameworks/four-test-types.md) - 探索找可能、诊断找原因、适用性确认能否满足具体镜头动作交付、运行检查重复复位搬运安装；开始前先写“这次是在找可能性、找原因，还是确认能用”。
* [试验判定的四种结果：满足当前条件／局部可用／不满足／证据不足](/frameworks/four-test-verdicts.md) - 判定不是只有通过或失败，每种结果都带下一动作与条件范围；“不喜欢”记为具体观看者偏好而非结构失败；艺术作品中的陌生不悦可能是任务一部分。

## 方法 · Method

* [区组、顺序与重复：让制作差异不被环境差异掩盖](/methods/blocking-order-repetition.md) - 借用 NIST 区组设计思想：同一时段内同时包含 A、B 再在另一时段复比；用中性编号与变换顺序减少“升级版”暗示；说清重复了什么（重播≠重复动作≠拆装重建）；少量结果不支持成功率。
* [颜色不对时先查链路，再决定重刷](/methods/color-chain-troubleshooting.md) - 颜色问题可能发生在物体、照明、摄影、处理与观看；先核样片与批准对象、同光同机位比较、再查输入解释与显示路径，最后才物理修改；ACES 区分输入／Look／输出，但不要求所有项目采用 ACES。
* [获取反馈，而不逼对方说出想听的答案](/methods/eliciting-feedback.md) - 先问先看见什么、何处变化被注意、何时认出产品／空间，再请对方用自己的语言描述感受并记录观看条件；区分项目确认者、专业同事与目标观看者；非商业作品不要求唯一解释；保存分歧比平均分有用。
* [修改后的回归检查：只复查受影响的链，不全案重审](/methods/regression-check-affected-chain.md) - 改一块材料先查它本身外观与动作，再查邻接、阴影、反射、接触和跨镜头状态；变更单写“受影响的消费方”；按依赖关系而非修改面积决定复查范围；保留旧版比较但只有一个当前批准依据。
* [单变量试验：适合局部定位，不是全部优化的唯一方法](/methods/single-variable-test-and-limits.md) - 问题可隔离时（如保护层是否导致过亮）比较同批次同基底同阶段的有无样片，固定光与拍摄；但单因素法无法揭示交互作用（NIST），要警惕在一种光下淘汰材料却从未在目标光下看过。
* [哪个试验先做：看后果、牵连与可逆性](/methods/test-priority-ordering.md) - 判断错误会不会换掉核心事件、会不会推翻空间或多人接口、能否便宜局部替换；次序为可发生性→最难观看条件→跨环节组合→运行与收尾；不算虚假风险系数，工程风险另由专业评价。
* [把问题写成能被证据回答的句子：对象、条件、改变、观察、决策](/methods/testable-question-sentence.md) - 弱问题“是不是更高级”→可测试问题“最终近景中 A、B 哪种表面让瓶体边缘清楚且背景不出抢眼亮斑”；观察项写可定位的事，并写明“这次不判断什么”。
* [四格组合试验：把材料与光放在一起比较](/methods/two-by-two-factorial-test.md) - 【本包设计的试验，未获数据】面层 A1/A2 × 照明 B1/B2 做全部四种组合；先按列比材料、按行比光，若最优材料随光改变则不能脱离照明回答；不算总分，按约束顺序选择；四格全不成立时检查变量范围或目标冲突。

## 原则 · Principle

* [何时停止测试：把资源留给仍有价值的问题](/principles/when-to-stop-testing.md) - 关键任务满足、运行条件已查、专业阻断已处理或明确、剩余修改主要是等价偏好交换时提交阶段确认；“没有任何未知”不是完成条件；放弃路线要留原因；区分概念、样片、指定镜头、工程确认四种完成范围。

## 检查清单 · Checklist

* [现场诊断：动作只能偶然成功](/checklists/field-diagnosis-accidental-action-success.md) - 检查起点、控制点、停点和复位参照，拆开不必联动的部分让关键物独立稳定；仍不可重复时缩小自由运动、换材料、固定体量承担轮廓或重新分配镜头任务；改变核心事件要回到概念确认。
* [现场诊断：画面越来越乱](/checklists/field-diagnosis-cluttered-image.md) - 先划出主体附近、动作经过处、必须保留的空场，暂时减少其中一项干扰再看完整观看顺序；不同问题需不同减法；每个物件都承担抽象价值时回到 01 的概念关系。
* [现场诊断：合成看起来贴在一起](/checklists/field-diagnosis-composite-looks-pasted.md) - 先看几何、前后遮挡、接触、反射和运动时序，再看颜色；没有正确接触关系时降低透明度只是遮盖；无素材可重建时明确缺口并提出补拍／重制，不保证“一键后期修复”。
* [现场诊断：材料像塑料、贴纸或纸片](/checklists/field-diagnosis-material-looks-plastic.md) - 分开检查形体厚度、边缘、接缝、纹理尺度与反射；把小块绕到最难角度看是哪处暴露基底——几何错改形体，均匀反射消除层次改环境或面层，最近镜头纹理不够就局部升级。
* [现场诊断：主体不突出](/checklists/field-diagnosis-subject-not-standing-out.md) - 先问主体是真不可辨还是只是不如预期抢眼、镜头是否确实要求突出；看轮廓遮挡、相邻明暗与反射，临时移除一个竞争物；依赖极强照明才能分开时检查空间和材料本身是否缺少区分。
* [十二种常见故障与第一项有用动作（含升级路线条件）](/checklists/twelve-common-faults-first-action.md) - 白物边缘消失、黑物无材质、金属盖映出器材、玻璃刻痕看不见、仿石像薄板、褶皱像废布、涂层后发亮、横版成立竖版堵塞、网纱纹理、图形像新贴、下一条状态对不上、导出后全变——各有优先区分项、第一项试验与升级路线条件；可能原因不是诊断结论。

## 模板 · Template

* [试验记录卡（05 篇交付模板）](/templates/experiment-record-card.md) - 试验标识、类型、要回答的问题、基准与保留项、改变的变量或组合、保持条件与干扰、步骤、观察与判定依据、实际材料与图像（未实施写未实施）、结果范围、解释、下一动作与受影响对象。
* [建立基准：六组条件的最少记录](/templates/test-baseline-record.md) - 改前／改后只有在已知差别下才有诊断价值；空间与对象、摄影、光与环境、材料、图像处理、使用六组各记最少信息；桌面练习可用固定手机与纸面标记，不写成精密色度测量；反光物周围拿走一张白纸也会改变外观。

## 练习 · Exercise

* [练习 A：一次局部诊断](/exercises/exercise-a-single-local-diagnosis.md) - 用非承重桌面物件与明暗卡建立基准，只移动一张卡记录物体哪部分改变；学会把环境变化对应到外观。
* [练习 B：四格表面—光试验](/exercises/exercise-b-four-cell-surface-light.md) - 用已知适合日常使用的纸或成品面材、两种表面×两个可恢复光向拍四格，写出材料选择是否依赖光；未出现明显差异也如实记录。
* [练习 C：复位不是重播](/exercises/exercise-c-reset-is-not-replay.md) - 用纸片设计开启—停留—复位；一次在原设置下重复、一次拆开后恢复，比较两种重复并修改定位与操作说明；桌面方法不能扩展成大型装置。

## 教学设定 · Teaching Scenario

* [一次完整现场回修：“方向对，但有点廉价，瓶盖很乱，布有点塌”](/cases/teaching-onset-revision-perfume-final-segment.md) - 【教学情境，未实拍】定位对象→冻结已成立部分→第一轮只处理反射→第二轮分开判断背景固定体量与运动片→第三轮组合回归→记录结论与未定项；未实测只能称回修计划。

# 关系

- 上一篇：[04 画面效果技法卡：二十种从机制、试做、调节到失效诊断的工作路径](/topics/04-effect-technique-cards.md)
- 下一篇：[06 真实制作案例与完整教学推演：看清方法怎样贯穿一个项目](/topics/06-real-cases-teaching-projects.md)
- 全包入口：[知识包总览](/index.md)
- 按问题找来源：[按问题组织来源：九类实际问题 → 优先来源 → 转成什么工作](/frameworks/sources-by-question-routing.md)

# Citations
[1] [05 测试、现场优化与回修 · 05_测试现场优化与回修](../../../美术创作与制作知识包_v2/05_测试现场优化与回修.md)
[2] [S04 What Do Prototypes Prototype?](/references/s04-houde-hill-what-do-prototypes-prototype.md)
[3] [S19 Silver Ain’t Steel — But It Can Be! How To Paint A Faux Steel Effect](/references/s19-powers-faux-steel.md)
[4] [S24 Painting The Heavenly Groundcloth for Earthquakes In London](/references/s24-powers-heavenly-groundcloth.md)
[5] [S28 Photographing A Flashlight](/references/s28-recher-photographing-flashlight.md)
[6] [S29 E-commerce White On White](/references/s29-recher-white-on-white.md)
[7] [S30 How to Photograph Engraved Glass](/references/s30-taylor-recher-engraved-glass.md)
[8] [S32 Roughness Using Microfacet Theory](/references/s32-pbrt-microfacet-roughness.md)
[9] [S34 5.2.1.2 One variable at a time](/references/s34-nist-one-variable-at-a-time.md)
[10] [S35 5.3.3.2 Randomized block designs](/references/s35-nist-randomized-block-designs.md)
[11] [S36 Input Transforms](/references/s36-aces-input-transforms.md)
[12] [S37 Look Transforms](/references/s37-aces-look-transforms.md)
[13] [S38 Output Transforms](/references/s38-aces-output-transforms.md)
[14] [S41 Safety in film, TV and broadcasting](/references/s41-hse-safety-film-tv.md)

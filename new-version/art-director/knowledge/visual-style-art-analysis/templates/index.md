# 模板与记录卡 · Templates

最小输出结构、观察记录、规则卡、交接卡、假设卡、方案卡、评价记录、决策卡等。


# 一 风格概念辨析与分面分析

* [词义与适用条件词条（不是风格词库）](term-meaning-condition-entry.md) - 一个词条至少保留：名称与词义、所属分面、适用范围、支持的特征组合、不能单独作为依据的特征、易混淆概念、相关案例、参考来源。
* [分面分析的最小输出结构（六部分）与一句话综合句式](six-part-minimal-output.md) - 分析范围、分面描述、主导组织规则、风格与参照判断、证据与替代解释、一句话综合描述；内部可细，呈现可压缩。

# 二 视觉观察与形式证据

* [单条观察记录（visual_observation）](visual-observation-record.md) - asset_version、scope、locator、observation、relation、interpretation、alternatives、not_observable、next_check；字段是表达约定，删字段不等于删证据边界。

# 三 混合风格与融合规则

* [参照单元记录：来源—所借特征—证据—作用范围—变换—未保留部分](reference-unit-record.md) - 一个来源不必是整个流派；“未保留部分”防止参考图不断获得额外权力，直到作品变成参考的变体。
* [混合视觉最小规则卡（hybrid_visual_rule）](hybrid-visual-rule-card.md) - scope、source_relations（参照／证据状态／所借关系）、transformation、organizing_rule、preserved、excluded、allowed_variations、exceptions、failure_condition。

# 四 美术工作与设计决策

* [变更说明四项：变化—受影响关系—受影响产物—待确认者](change-impact-four-items.md) - 把台座加高可能改变包装比例、反光、遮挡、演员动作和机位；变更必须带着影响范围传播，确实受影响的消费者不能只收到一句“已更新”。
* [不虚构幕后事实的美术分析三栏：可见设计选择／可成立的实现候选／已核实的制作事实](three-column-art-analysis.md) - 没有资料时第三栏不需要通过多写候选把它伪装填满；“可能做了”与“实际做了”在标题上分开。
* [美术决策最小交接卡（art_design_decision）](art-design-decision-handoff-card.md) - purpose、current_decision、scope、visual_constraints、use_constraints、implementation_status、evidence、consumer、acceptance_check、change_impact。

# 五 创作出发点与解释边界

* [假设矩阵：候选解释、目前支持、可能削弱的证据、值得寻找的资料](hypothesis-matrix.md) - 对关键现象只保留少数有区分价值的候选；以“人物长期位于画面边缘”为例；候选不一定互斥，可得出“多因素共同作用”。
* [最小假设卡：claim_type、question、scope、hypothesis、支持、替代、反证、改变条件、状态](hypothesis-card.md) - 状态描述适用于某条主张而非整件作品；解释被撤回不意味原始观察被删除；原始材料错误则相关解释需回查。

# 六 从抽象需求到场景方案

* [最小方案卡（visual_scene_concept）](visual-scene-concept-card.md) - task、confirmed_constraints、assumptions、concept、core_relations、scene_and_action、references（source/borrow/exclude）、prototype_question、acceptance_basis、approval_scope、next_decision。

# 七 作品评价与反馈验证

* [五段式反馈：画面证据 → 可能影响 → 所依赖目标或条件 → 建议动作 → 复查方式](five-part-feedback.md) - 以瓶身右边缘与弧形高光重叠为例；“可能构成干扰”是基于关系的风险判断；局部问题不扩成“整套不高级，全部重做”。
* [最小评价记录（虚构模板）](evaluation-record.md) - work_version、scope、purpose、criterion（name/reason）、observation（statement/source）、judgment（status/statement/limitation）、preserve、candidate_change、verification、approval_scope。

# 八 分析沉淀与知识复用

* [关键设计决策卡：十个栏目](key-design-decision-card.md) - 对象与范围、可见证据、关键选择、作用解释、证据身份、其他解释、可迁移部分、不变量与变量、失效条件、验证与版本；每件作品先挑三到五个真正决定呈现的选择（起点，不是固定数量）。
* [规则卡句式：带条件的提议](rule-card-sentence.md) - 当任务出现____问题时，可以尝试通过____关系，而不是只增加____元素，来形成____的候选效果；需要保留____；可以改变____；在____条件下可能失效，需用____检查。
* [关键概念的编码说明（含正例、反例、难判案例）](coding-note.md) - 以“主体隔离”为例：指位置、边界或注意层次上的分离而非物件少；可接受哪些证据、哪些相似情况不计入、局部与整体如何区分；一致性高不自动等于判断正确。
* [最小结构化知识记录（虚构教学模板）](structured-knowledge-record.md) - record_id/version/kind、source（asset_id/version/available_material/locator）、scope、observation、interpretations（含 author 与 alternatives）、production_fact、transfer_rule、validation、active_project_decision；未知保持 null。

# 来源与边界：官方文档说了什么、借了哪些理论、什么不能声称

## 这个 skill 依据什么

- **用户资料**：13 组 AI 影视教程的文字复审稿（原仓库 ALBEDO-TABAI/ciwei-ai-shortfilm-notes，固定版本 `5887b20`）。提供问题样本。
- **官方文档**：下面列的工具文档，访问日期 2026-09-17。网页会更新，用前重新核对。
- **本次综合**：六个问题、三种稿子、两张图谱、模板、练习、案例——全部是设计，**没有跑过生成实验**。

## 图像工具官方文档

| 来源 | 说了什么 | 用它反对什么 | 不能推出 |
| --- | --- | --- | --- |
| [Midjourney Prompt Basics](https://docs.midjourney.com/hc/en-us/articles/32023408776205-Prompt-Basics) | 简洁清楚，短句往往比长清单合适 | "当代提示词必须全部改成长段自然语言" | 某模型更强；删某词一定改善 |
| [Google Gemini 图像生成](https://ai.google.dev/gemini-api/docs/image-generation) | 用主体、媒介、细节、修改目标组织 | 只把句子变长 | 每个接口都能分离身份风格布局 |
| [OpenAI Image generation](https://developers.openai.com/api/docs/guides/image-generation) | 蒙版可指导编辑但形状不一定被精确遵循 | "写绝对不变就能像素级保证" | 所有系统用相同蒙版机制 |
| [Runway Gen-4 Image](https://help.runwayml.com/hc/en-us/articles/35694045317139-Gen-4-Image-Prompting-Guide) | 同时讨论描述句和关键词 | "新派/旧派写法"二分 | 该公司全部模型规则 |

## 视频工具官方文档

| 来源 | 说了什么 | 这里怎么用 | 不能推出 |
| --- | --- | --- | --- |
| [Runway Image to Video](https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide) | 输入图是静态条件，提示词描述运动和时间 | 区分首帧接续和从零生视频 | 所有身份参考等于首帧；文字总能覆盖参考图 |
| [Runway Text to Video](https://help.runwayml.com/hc/en-us/articles/42460036199443-Text-to-Video-Prompting-Guide) / [Intro](https://help.runwayml.com/hc/en-us/articles/46182941379347-Introduction-to-Prompting) | 清楚描述、时间安排、渐进迭代 | 简洁起步按任务加信息 | 某个长度是唯一规则 |
| [Runway Gen-4 Video](https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide) | 偏向正向表述，从简单动作逐步加 | 否定句转正向的做法 | **所有视频模型不支持负向提示** |
| [Google 视频提示指南](https://cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide) | 按主体动作环境拍摄方式组织；部分高级镜头效果可靠性可能变化 | 镜头移动旋转变焦分开写 | 写焦距就得到准确透视 |
| [OpenAI Sora2 Guide（已归档）](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide) | "详细控制和创作开放都可有效，提示是指导不是保证" | 只借这个创作层思路 | 当前产品可用性、规格、价格 |

## 配音和灯光

- [ElevenLabs 停顿](https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/how-can-i-add-pauses) / [SSML 与 API](https://elevenlabs.io/docs/help-center/technical/do-pauses-and-ssml-phoneme-tags-work-with-the-api)：不同模型停顿控制方式不同；标点停顿不如专门控制稳定。→ 别把"……"当跨工具固定 0.3 秒。
- [Blender 5.2 Light Objects](https://docs.blender.org/manual/nl/5.2/render/lights/light_object.html)：功率和尺寸分开说明，尺寸影响阴影软硬。→ 硬光不等于亮；百叶窗不是硬光前提。

## 理论桥梁（各支持一座小桥，不是总证明）

- **Palmer et al. 2013, PNAS**（[doi](https://doi.org/10.1073/pnas.1212562110)）：音乐—颜色配对与共有情绪维度有关。→ 构思音乐颜色材料时先找共享的重量明暗活跃度张力。不是"蓝色=悲伤"。
- **Don Norman, Signifiers not affordances**（[链接](https://jnd.org/signifiers-not-affordances/)）：区分"能做什么"和"怎么感知到能做什么"。→ 门把、空椅、使用痕迹给角色可做的事、给观众解释入口。
- **Tim J. Smith, Watching you watch There Will Be Blood**（[链接](https://www.davidbordwell.net/blog/2011/02/14/watching-you-watch-there-will-be-blood/)）：11 名观众的眼动观察。→ 关键动作要有机会被看到；这是检查方法不是保证。
- **David Bordwell, Hands (and faces) across the table**（[链接](https://www.davidbordwell.net/blog/2008/02/13/hands-and-faces-across-the-table/)）：镜头内部组织本身有表达能力。→ 固定镜头可以靠人物物件声音组织注意力。

## 五条推论（本 skill 提出，待检验）

1. 表达是一对多，不是找唯一咒语
2. 具体不是越多越好，而是减少关键歧义
3. 一致性是关系持续，不只是长相不变
4. 通感允许差异，不要求各部门齐声
5. 提示词实践是反馈循环，不是一次性写作

## 不得声称

- 没读到的图、没听到的音频→不得宣布验收
- 文件名≠已上传；编号≠已绑定；文字秒数≠真实参数；提交成功≠媒体通过
- 设备名是外观联想，不是调用物理相机
- 不知道具体模型内部为什么偏好某个词
- 没有"模型按提示词顺序逐句执行摄影机和演员动作"的证据
- 案例是设计样稿，不是实测结果
- 没有模型排名、价格、限额、保证时长

# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""A file containing prompts definition."""

CLAIM_EXTRACTION_PROMPT = """
-目标活动-
你是一位智能助手，帮助人类分析师分析文本文档中针对特定实体的声明。

-目标-
给定一个与此活动潜在相关的文本文档、实体规范和声明描述，提取所有符合实体规范的实体以及针对这些实体的所有声明。

-步骤-
1. 提取所有符合预定义实体规范的命名实体。实体规范可以是实体名称列表或实体类型列表。

2. 对于步骤1中识别的每个实体，提取与该实体相关的所有声明。声明需要符合指定的声明描述，且实体应为声明的主体。
   对于每个声明，提取以下信息：
   - 主体：声明主体的实体名称。主体实体是执行声明中描述的行为的实体。主体需要是步骤1中识别的命名实体之一。
   - 客体：声明客体的实体名称。客体实体是报告/处理声明中描述的行为或受其影响的实体。如果客体实体未知，使用**NONE**。
   - 声明类型：声明的总体类别。以可在多个文本输入中重复使用的方式命名，使相似的声明共享相同的声明类型。
   - 声明状态：**TRUE**、**FALSE**或**SUSPECTED**。TRUE表示声明已确认，FALSE表示声明被证实为假，SUSPECTED表示声明未经验证。
   - 声明描述：详细解释声明背后的推理，包括所有相关证据和参考资料。
   - 声明日期：声明发生的时期（开始日期，结束日期）。开始日期和结束日期都应采用ISO-8601格式。如果声明发生在单一日期而非日期范围内，则开始日期和结束日期设置为相同日期。如果日期未知，返回**NONE**。
   - 声明源文本：原文中与声明相关的**所有**引用列表。

   按以下格式化每个声明：(<主体实体>{tuple_delimiter}<客体实体>{tuple_delimiter}<声明类型>{tuple_delimiter}<声明状态>{tuple_delimiter}<声明开始日期>{tuple_delimiter}<声明结束日期>{tuple_delimiter}<声明描述>{tuple_delimiter}<声明源>)

3. 以中文返回输出，作为步骤1和2中识别的所有声明的单一列表。使用**{record_delimiter}**作为列表分隔符。

4. 完成后，输出{completion_delimiter}

-示例-  

示例：
实体规范：冯宝宝，徐家夫妇，赵嫂
声明描述：与实体相关的声明或事实
文本：1944年夏，冯宝宝身着旗袍、脚踩高跟鞋，在四川的山洞中苏醒。她在山道上迷茫徘徊，险遭路人侵犯，幸得徐家夫妇相救，被赵嫂带回家中。
输出：
(冯宝宝{tuple_delimiter}NONE{tuple_delimiter}苏醒{tuple_delimiter}TRUE{tuple_delimiter}1944-06-01T00:00:00{tuple_delimiter}1944-08-31T00:00:00{tuple_delimiter}冯宝宝在1944年夏天苏醒{tuple_delimiter}1944年夏，冯宝宝在四川的山洞中苏醒。)
{record_delimiter}
(冯宝宝{tuple_delimiter}路人{tuple_delimiter}险遭侵犯{tuple_delimiter}TRUE{tuple_delimiter}1944-06-01T00:00:00{tuple_delimiter}1944-08-31T00:00:00{tuple_delimiter}冯宝宝在山道上迷茫徘徊，险遭路人侵犯{tuple_delimiter}她在山道上迷茫徘徊，险遭路人侵犯。)
{record_delimiter}
(冯宝宝{tuple_delimiter}徐家夫妇{tuple_delimiter}相救{tuple_delimiter}TRUE{tuple_delimiter}1944-06-01T00:00:00{tuple_delimiter}1944-08-31T00:00:00{tuple_delimiter}徐家夫妇相救冯宝宝{tuple_delimiter}幸得徐家夫妇相救，)
{record_delimiter}
(冯宝宝{tuple_delimiter}李嫂{tuple_delimiter}带回家中{tuple_delimiter}FALSE{tuple_delimiter}1944-06-01T00:00:00{tuple_delimiter}1944-08-31T00:00:00{tuple_delimiter}赵嫂带冯宝宝回家中{tuple_delimiter}被赵嫂带回家中。)

-实际数据-
请使用以下输入作为您的答案。
实体规范：{entity_specs}
声明描述：{claim_description}
文本：{input_text}
输出："""


CONTINUE_PROMPT = "在最后一次提取中，许多实体被遗漏了，请使用相同的格式在下面添加它们:\n"
#LOOP_PROMPT = "It appears some entities may have still been missed.  Answer YES {tuple_delimiter} NO if there are still entities that need to be added.\n"
LOOP_PROMPT = "可能仍有一些实体被遗漏了，如果仍然有需要添加的实体，请回答YES {tuple_delimiter}NO。\n"

# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""A file containing prompts definition."""

GRAPH_EXTRACTION_PROMPT = """

-目标-
给定一个角色百科文档或剧情摘要概述以及一个实体类型列表，从文本中识别所有这些类型的实体及实体之间的所有关系。

-步骤-
1. 识别所有实体。对于每个识别出的实体，提取以下信息：
- 实体名称：实体名称，不允许为空。
- 实体类型：以下类型之一：[{entity_types}]，不允许为空。
- 实体描述：实体属性和活动的全面描述，不允许为空。
 格式化每个实体为 ("entity"{tuple_delimiter}<实体名称>{tuple_delimiter}<实体类型>{tuple_delimiter}<实体描述>)

2. 从步骤1中识别的实体中，识别所有 **彼此明确相关** 的 (源实体, 目标实体)
对于每对相关的实体，提取以下信息：
- 源实体：在步骤1中识别出的源实体名称，不允许为空。
- 目标实体：在步骤1中识别出的目标实体名称，不允许为空。
- 关系描述：思考并解释为什么你认为源实体和目标实体彼此相关，不允许为空。
- 关系强度：一个介于1到10之间的整数分数，表示源实体和目标实体之间关系的强度，不允许为空。
 格式化每个关系为 ("relationship"{tuple_delimiter}<源实体>{tuple_delimiter}<目标实体>{tuple_delimiter}<关系描述>{tuple_delimiter}<关系强度>)

3. 返回输出中文，作为步骤1和2中识别的所有实体和关系的单一列表。使用 **{record_delimiter}** 作为列表分隔符。

4. 完成后，输出 {completion_delimiter}

######################
-示例-
######################
# 示例1：
实体类型：[组织,时间,人物,地点,事件]
正文：
1944年夏，冯宝宝身着旗袍、脚踩高跟鞋，在四川的山洞中苏醒。她在山道上迷茫徘徊，险遭路人侵犯，幸得徐家夫妇相救，被赵嫂带回家中。在赵嫂的悉心教导下，冯宝宝迅速学会了说话和写字，然而她对自己的过去一无所知，除了名字外，村民们便称她为阿无。尽管失去了记忆和情感，阿无在徐家却过得安逸自在，甚至指导徐家的儿子徐翔修炼炁。然而，1949年春，阿无的平静生活被打破。土匪闯入村庄，杀害了徐父。在赵嫂的愤怒驱使下，阿无在众目睽睽之下斩杀了所有土匪。但因她容颜不老，被村民视为妖怪而遭受排斥。赵嫂骗她到山中躲藏两日，却带着徐翔离去。孤独的阿无在山中独自生活了几十年，为了生存甚至与大熊猫争夺食物。
===
输出：
("entity"{tuple_delimiter}1944年夏{tuple_delimiter}时间{tuple_delimiter}冯宝宝在四川的山洞中苏醒。){record_delimiter}
("entity"{tuple_delimiter}冯宝宝{tuple_delimiter}人物{tuple_delimiter}身着旗袍、脚踩高跟鞋，在四川的山洞中苏醒。她在山道上迷茫徘徊，险遭路人侵犯，幸得徐家夫妇相救，被赵嫂带回家中。在赵嫂的悉心教导下，冯宝宝迅速学会了说话和写字，然而她对自己的过去一无所知，除了名字外，村民们便称她为阿无。){record_delimiter}
("entity"{tuple_delimiter}四川{tuple_delimiter}地点{tuple_delimiter}冯宝宝在四川的山洞中苏醒。){record_delimiter}
("entity"{tuple_delimiter}徐家夫妇{tuple_delimiter}人物{tuple_delimiter}在冯宝宝险遭路人侵犯时相救。){record_delimiter}
("entity"{tuple_delimiter}赵嫂{tuple_delimiter}人物{tuple_delimiter}在冯宝宝险遭路人侵犯时带她回家中，并悉心教导她迅速学会了说话和写字。){record_delimiter}
("entity"{tuple_delimiter}阿无{tuple_delimiter}人物{tuple_delimiter}失去了记忆和情感，尽管如此，在徐家过得安逸自在，甚至指导徐家的儿子徐翔修炼炁。){record_delimiter}
("entity"{tuple_delimiter}徐翔{tuple_delimiter}人物{tuple_delimiter}徐家的儿子，阿无指导他修炼炁。){record_delimiter}
("entity"{tuple_delimiter}1949年春{tuple_delimiter}时间{tuple_delimiter}土匪闯入村庄，杀害了徐父，阿无的平静生活被打破。){record_delimiter}
("entity"{tuple_delimiter}土匪{tuple_delimiter}组织{tuple_delimiter}1949年春，闯入村庄，杀害了徐父。){record_delimiter}
("entity"{tuple_delimiter}徐父{tuple_delimiter}人物{tuple_delimiter}1949年春，被土匪杀害。){record_delimiter}
("relationship"{tuple_delimiter}冯宝宝{tuple_delimiter}赵嫂{tuple_delimiter}赵嫂带冯宝宝回家中，并悉心教导她迅速学会了说话和写字。{tuple_delimiter}8){record_delimiter}
("relationship"{tuple_delimiter}阿无{tuple_delimiter}徐翔{tuple_delimiter}阿无指导徐翔修炼炁。{tuple_delimiter}7){record_delimiter}
("relationship"{tuple_delimiter}阿无{tuple_delimiter}徐家夫妇{tuple_delimiter}徐家夫妇救了阿无并收留了她。{tuple_delimiter}7){record_delimiter}
("relationship"{tuple_delimiter}赵嫂{tuple_delimiter}徐家夫妇{tuple_delimiter}赵嫂住在徐家并帮助照顾阿无。{tuple_delimiter}6){record_delimiter}
("relationship"{tuple_delimiter}土匪{tuple_delimiter}徐父{tuple_delimiter}土匪杀害了徐父。{tuple_delimiter}9){record_delimiter}
("relationship"{tuple_delimiter}冯宝宝{tuple_delimiter}阿无{tuple_delimiter}冯宝宝失去了记忆和情感，被村民们称为阿无。{tuple_delimiter}10){record_delimiter}
{completion_delimiter}
 
######################  
-真实数据-
######################  

实体类型: {entity_types}
正文: {input_text}

===
输出:"""

#CONTINUE_PROMPT = "MANY entities were missed in the last extraction.  Add them below using the same format:\n"
#LOOP_PROMPT = "It appears some entities may have still been missed.  Answer YES | NO if there are still entities that need to be added.\n"
CONTINUE_PROMPT = "在最后一次提取中，许多实体被遗漏了，请使用相同的格式在下面添加它们:\n"
LOOP_PROMPT = "可能仍有一些实体被遗漏了，如果仍然有需要添加的实体，请回答YES | NO。\n"

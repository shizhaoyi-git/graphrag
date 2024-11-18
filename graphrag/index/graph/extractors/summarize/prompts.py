# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""A file containing prompts definition."""

SUMMARIZE_PROMPT = """
你是一位负责生成以下数据的全面摘要的助手。
给定一个或两个实体，以及一系列描述，这些描述都与同一个实体或一组实体相关。
请将所有这些描述合并为一个完整的描述，确保包括所有描述中收集到的信息，但不要存在与描述列表中内容无关的信息。
如果提供的描述存在矛盾，请解决这些矛盾并提供一个连贯的摘要。
确保使用第三人称书写，并包括实体名称以确保我们有完整的上下文。

######################
-示例-
######################
示例1：

实体："暗堡"
描述列表: ["告诉了张楚岚等人关于暗堡的事。", "哪都通的设施，廖忠和老孟将陈朵带回此地。", "废弃的建筑，角色和其他临时工、张楚岚以及张灵玉在此等待马仙洪。", "廖忠长时间居住的地方，也是哪都通华南大区的管理地点之一，负责相关工作。", "由廖忠负责的地点，风波命女医生被送入的地方。", "神秘的地点，蛊身圣童被安置于此，暗堡的人通过各种方法帮助圣童恢复人性。", "陆玲珑与陆琳一起盯着张楚岚的地点。", "陈俊彦与陈朵结识的地点，也是观察陈俊彦异能的场所。", "陈朵不愿再回到这里。", "陈朵和陈俊彦相识的地方。", "陈朵被隔离和训练的地点，后成为她想要离开的地方。"]

######################
输出：
暗堡，一个由哪都通公司管理的废弃建筑，既是其华南大区的运营点之一，也是廖忠长期居住和负责的地点。此地曾是陈朵被带回并隔离训练的地方，由廖忠和老孟将她带至此地。暗堡也是张楚岚、张灵玉和其他临时工等待马仙洪的地点，同时，它还是蛊身圣童被安置之处，暗堡的人通过各种方法帮助圣童恢复人性。陆玲珑与陆琳曾在此地监视张楚岚。陈俊彦与陈朵在此相识，暗堡亦是观察陈俊彦异能的场所。然而，陈朵对这个地方有着复杂的情感，她不愿再回到这里，因为暗堡最终成为了她想要逃离的地方。风波命女医生也被送入暗堡，由廖忠负责。暗堡的多重角色和复杂历史，使其成为一个充满神秘色彩的地点。

######################
-真实数据-
######################
实体：{entity_name}
描述列表：{description_list}
######################
输出：
"""

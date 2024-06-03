generate_scenario = '''Now I need your help to complete a scene mining task for a dataset. I will provide you with a dataset of 【${description}】, and your role will be defined as 【${profile}】. Based on several data points, please explore potential data scenarios. The data scenarios you generate should adhere to the following guidelines: 【${reminder}】. Now, please generate a data scenario based on the 【${oddClickedNodesString}】 from dataset. Pay attention to the characteristics of the data and the guidelines for generating data scenarios.
Please return in the following format: 
1、Data Scenario (a brief summary in a few sentences):
2、Involved Variables (what variables/data are needed to complete this scenario):
3、Reasoning Logic (why you thought of this scenario):
4、Application Scenario (its practical significance):'''
feedback = '''Thank you for the data scenario you generated. Upon inspection, it appears that there may be the following issues with the scenario: 【${reminderText}】. Please carefully consider and generate a new data scenario to address the aforementioned problems.'''
add_node = '''Please extract the new variables involved in the data scenario you generated and return them to me in the format of ${JSON.stringify(oddClickedNodes.value, null, 2)} (This is the initial variable I provided to you, please do not include these variables in the first JSON.).

At the same time, please establish relationships between the newly extracted variables and the initial variables (select from ${JSON.stringify(oddClickedNodes.value, null, 2)}) I provided to you, in the following format: {"source": X, "target": X, "value": X}. Here, 'source' represents the variables I provided to you, 'target' refers to the new variables involved in your data scenario, and 'value' is your assessment of the correlation between the two, ranging from 1 to 5.

So, in the end, you need to return to me two JSON objects, one storing the variables and the other storing the relationships between the old and new variables.'''

import streamlit as st

DATA_DESCRIPTION_PROMPT = '''You are given a list of data items with their names, types, and examples in JSON format as <input>. Your task is to generate a detailed description for each data item as <output> in JSON format. The description should explain what the data item represents and provide context on its usage or significance.
<input>
{{
  "UserID": {{
    "type": "Integer",
    "example": 1024
  }},
  "Username": {{
    "type": "String",
    "example": "john_doe"
  }},
  "AccountBalance": {{
    "type": "Float",
    "example": 250.75
  }},
  "SignupDate": {{
    "type": "Date",
    "example": "2023-01-15"
  }}
}}
<output>
{{
  "UserID": "The UserID is a unique identifier assigned to each user in the system. It is an integer value that ensures each user can be distinctly recognized. This identifier is crucial for linking user-related data across various tables and functionalities within the database.",
  "Username": "The Username is a string that represents the name chosen by the user to identify themselves on the platform. It is used for logging in and personalizing the user experience. Usernames must be unique across the system to prevent conflicts and ensure each user has a distinct identity.",
  "AccountBalance": "The AccountBalance is a float value indicating the current balance in the user's account. It represents the amount of money available for transactions and is updated in real-time with each deposit or withdrawal. This balance is crucial for financial tracking and ensuring users can manage their funds effectively.",
  "SignupDate": "The SignupDate is the date on which the user registered on the platform. It is stored in the Date format and helps in tracking user activity and tenure. Understanding the SignupDate is important for analyzing user engagement trends and managing promotions or loyalty programs."
}}
<input>
{}
<output>
'''

GENERATE_SCENARIO_SYSTEM_PROMPT = '''You are a scholar specializing in empirical research, capable of discovering research-worthy scenarios from existing data.
The user's input consists of multiple data items from one or more data files, organized in JSON format as shown in the <Example Input>. Each data item includes a name, type, description (which may be empty), and example. 
Your task is to analyze the relationships between different data files and data items, and generate a valuable research scenario based on the json format in the <Example Output> includes:
1、Scenario Name
2、Scenario Description (a brief summary in a few sentences)
3、Involved Variables (what variables/data are needed to complete this scenario)
4、Reasoning Logic (why you thought of this scenario)
5、Application Scenario (its practical significance)
Please follow the above requirements, consider the scenario requirements in the <User Guidance>, and generate a data scenario based on the <User Input>.
<Example Input>
{
   "example_dataset.csv":[
      {
         "name":"PatternID",
         "type":"int64",
         "description":"",
         "example":1
      },
      {
         "name":"PatternName",
         "type":"object",
         "description":"",
         "example":"Geometric Bliss"
      },
      {
         "name":"PatternType",
         "type":"object",
         "description":"",
         "example":"geometric"
      },
      ...
   ],
   ...
}

<Example Output>
{
    "Scenario Name":"...",
    "Scenario Description":"...",
    "Involved Variables":"...",
    "Reasoning Logic":"...",
    "Application Scenario":"..."
}
'''
from langchain_openai import ChatOpenAI
import streamlit as st
# from prompt import DATA_DESCRIPTION_PROMPT

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
MODELS = ['gpt-3.5-turbo', 'gpt-3.5-turbo-1106', 'gpt-4', 'gpt-4-turbo', 'gpt-4-1106-preview']

class LLM:
    def __init__(self, api_key: str, temperature: float = 0.7, model_name: str = 'gpt-3.5-turbo', openai_api_base=None):
        self.api_key = api_key
        self.temperature = temperature
        self.model_name = model_name
        self.openai_api_base = openai_api_base
        self.llm = ChatOpenAI(api_key=self.api_key, temperature=self.temperature, model=self.model_name, openai_api_base=self.openai_api_base)

    def invoke(self, system_prompt: str, human_prompt: str) -> str:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": human_prompt}
        ]
        response = self.llm.invoke(messages)
        return response.content
    
    def test_available(self):
        system_prompt = "You are a helpful assistant."
        human_prompt = "What is the capital of France?"
        response = self.invoke(system_prompt, human_prompt)
        return isinstance(response, str) and len(response) > 0
    
def data_description_generation(item_df):
    if not st.session_state.get('llm'):
        st.toast("LLM is not available. Please check your settings.")
        return
    item_dict = {}
    for index, row in item_df.iterrows():
        column = row['column']
        item_dict[column] = {col: row[col] for col in item_df.columns if col != 'column' and col != 'description'}
    res = st.session_state.llm.invoke('', DATA_DESCRIPTION_PROMPT.format(item_dict))
    res = eval(res)
    for name, desc in res.items():
        item_df.loc[item_df['column'] == name, 'description'] = desc
    return item_df
    
def data_relationship_generation():
    pass
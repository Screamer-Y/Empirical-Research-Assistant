from langchain_openai import ChatOpenAI
import streamlit as st

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
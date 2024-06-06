import streamlit as st

DATA_DESCRIPTION_PROMPT = '''You are given a list of data items with their names, types, and examples in JSON format as <input>. Your task is to generate a detailed description for each data item as <output> in JSON format. The description should explain what the data item represents and provide context on its usage or significance.
<input>
{
  "UserID": {
    "type": "Integer",
    "example": 1024
  },
  "Username": {
    "type": "String",
    "example": "john_doe"
  },
  "AccountBalance": {
    "type": "Float",
    "example": 250.75
  },
  "SignupDate": {
    "type": "Date",
    "example": "2023-01-15"
  }
}
<output>
{
  "UserID": "The UserID is a unique identifier assigned to each user in the system. It is an integer value that ensures each user can be distinctly recognized. This identifier is crucial for linking user-related data across various tables and functionalities within the database.",
  "Username": "The Username is a string that represents the name chosen by the user to identify themselves on the platform. It is used for logging in and personalizing the user experience. Usernames must be unique across the system to prevent conflicts and ensure each user has a distinct identity.",
  "AccountBalance": "The AccountBalance is a float value indicating the current balance in the user's account. It represents the amount of money available for transactions and is updated in real-time with each deposit or withdrawal. This balance is crucial for financial tracking and ensuring users can manage their funds effectively.",
  "SignupDate": "The SignupDate is the date on which the user registered on the platform. It is stored in the Date format and helps in tracking user activity and tenure. Understanding the SignupDate is important for analyzing user engagement trends and managing promotions or loyalty programs."
}
<input>
{}
<output>
'''
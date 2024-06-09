import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Access environment variables
API_KEY = os.getenv('API_KEY')

# Initialize OpenAI Client
client = OpenAI(api_key=API_KEY)

# Generates AI request
def ask_GPT(user_prompt: str):
    """
    Normal GPT Parsing

    Problem 1 : Dude can't remember interactions

    """

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "A programer will prompt you his goal, propose a small step-by-step to solve his problem."},
        {"role": "user", "content": user_prompt}
        ],
    )

    print(completion.choices[0].message.content)

# Generates Command Parsing Request
def ask_command_parser(user_prompt: str):
    """
    Konsole Command Parser

    """

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = [

            { "role": "system", 
            "content": "A programer will prompt you his goal, propose a small step-by-step to solve his problem."},

            { "role": "user", 
              "content": user_prompt}
        ],
    )

    print(completion.choices[0].message.content)

# Confirms Command Parsing Request
def confirm_command_parser(user_prompt: str):
    """
    Confirms commands

    """

    user_wants_to_proceed = input("Should we proceed with the installation? [Y\\N]")

    if user_wants_to_proceed == "Y" or user_wants_to_proceed == "y":
        execute_command_parser(user_prompt)
    elif user_wants_to_proceed == "N" or user_wants_to_proceed == "n":
        return
    else:
        confirm_command_parser(user_prompt)

# Executes Command Parsing Request
def execute_command_parser(user_prompt):
    pass
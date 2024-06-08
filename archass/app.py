import os
from dotenv import load_dotenv
from openai import OpenAI

# import utilities
import utils.commands as commands
import utils.prompts as prompts

# import global variables
import config

# Load environment variables from .env file
load_dotenv()

# Access environment variables
API_KEY = os.getenv('API_KEY')

# Initialize OpenAI Client
client = OpenAI(api_key=API_KEY)

# Initialize global variables
config.RUNNING = True

def main():
    while config.RUNNING:
        # Prompt the user
        user_prompt = input("wtv ... : ")
        prompts.process_user_prompt(user_prompt)

if __name__ == "__main__":
    main()


# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ],
# )

# print(completion.choices[0].message.content)
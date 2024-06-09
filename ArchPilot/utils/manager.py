import os
from dotenv import load_dotenv
from openai import OpenAI

from . import db

# Load environment variables from .env file
load_dotenv()

# Access environment variables
API_KEY = os.getenv('API_KEY')

# Initialize OpenAI Client
client = OpenAI(api_key=API_KEY)

# Load Conversations
conversations = db.conversation_history

# Roles
alex_role = "does almost everything"
bob_role = "..."
carl_role = "if asked explicitely, will parse commands directly to the Konsole"

# System's role
system_role = """ 
                    You are tasked with determining the most suitable employee to assign a specific responsibility based on their job roles. 
                    
                    Here is a brief overview of each employee's responsibilities:

                    - Alex: {alex_role}
                    - Bob: {bob_role}
                    - Carl: {carl_role}

                    Given a task, decide which employee is best suited to handle it. 
                    
                    You should respond with only one word, the name of the employee. 
                    The possible choices are Alex, Bob.

              """

# Only chooses employee based on user input
def managerGPT(user_prompt: str):
    """

    Manager GPT with bad memory.

    """

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": system_role },
            {"role": "user", "content": user_prompt }
        ],
    )

    return completion.choices[0].message.content
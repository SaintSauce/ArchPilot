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

# Add Entry
def addEntry(role: str, content: str):
    """
    
    Adds entry to conversation history

    """
    db.conversation_history.append(
        {"role" : role, "content" : content}
    )

# Assign Task to AI
def assignTask(task: str):
    """
    
    Assigns task to AI

    Use it carefully

    """
    addEntry("system", task)

# Normal Awareness Request
def askGPT(user_prompt: str):
    """

    Alex the Normal GPT Parsing

    """

    addEntry("user", user_prompt)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversations,
    )

    print(completion.choices[0].message.content)

# Package Manager Request
def pacmanGPT(user_prompt: str):
    """

    Bob the Package Manager GPT

    """

    assignTask("Take the necessary packages and output them in the format \"package_1\", \"package_2\", ..., \"package_N\"")

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversations,
    )

    print("Do you want to download these packages ...")
    print(completion.choices[0].message.content)

# Package Manager Request
def executionnerGPT(user_prompt: str):
    """

    Carl the Command Executionner GPT

    """

    assignTask("Take the necessary commands based on the wanted packages and output them in the format \"package_1\", \"package_2\", ..., \"package_N\"")

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversations,
    )

    print(completion.choices[0].message.content)
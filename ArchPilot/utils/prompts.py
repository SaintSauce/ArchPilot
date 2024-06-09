from . import tools
from . import commands

def process_user_prompt(user_prompt: str):
    """
    Processes the user's prompt

    Do's and dont's.

    Does necessary stuff.

    """

    # exit Konsole
    if user_prompt == "exit":
        tools.terminate_program()
    
    return user_prompt
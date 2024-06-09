from . import tools
from . import employees as chat
from . import commands as command

def process_user_prompt(user_prompt: str):
    """
    
    Processes the user's prompt

    Do's and dont's.

    """

    # exit Konsole
    if user_prompt == "exit":
        tools.terminate_program()
    
    if user_prompt == "clean":
        command.run_command("clear")
    
    # maybe process some more
    
    return user_prompt
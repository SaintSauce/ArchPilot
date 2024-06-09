# import global variables
import config

# other stuff
from . import prompts as prompt
from . import commands as command
from . import employees as chat
from . import manager

# Initialize global variables
RUNNING = True

def arch_pilot():
    """
    
    Initialize ArchPilot

    """

    command.run_command("clear")

    while RUNNING:
            # Prompt the user
            user_prompt = input(config.SHELL_NAME + ": ")
            proc_output = prompt.process_user_prompt(user_prompt)
            
            # Dispatch employee based on intent
            man_of_the_hour = manager.managerGPT(proc_output)

            if man_of_the_hour == "Alex":
                print("I am Alex")
                chat.askGPT(user_prompt)
            elif man_of_the_hour == "Bob":
                print("I am Bob")
                chat.pacmanGPT(user_prompt)
            elif man_of_the_hour == "Carl":
                print("I am Carl")
                chat.executionnerGPT(user_prompt)
import config

from . import commands
from . import prompts

"""

Notes. Needs to be the most encapsulated file.

"""

def terminate_program():
    """
    Sends a signal to exit the Konsole

    Probably just terminate main.

    """

    commands.run_command("clear")
    commands.run_command("ls")

    for i in range(20):
        print("          ")
    
    print("--------------------------------")
    print("---------- Peace out! ----------")
    print("--------------------------------")

    for i in range(5):
        print("          ")
    
    config.RUNNING = False
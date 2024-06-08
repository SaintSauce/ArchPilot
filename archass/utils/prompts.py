from tools import terminate_program

def process_user_prompt(prompt: str) -> str:
    """
    Processes the user's prompt

    Do's and dont's.

    """

    # exit Konsole
    if prompt == "exit":
        terminate_program()

    return prompt
import utils

def process_user_prompt(prompt: str):
    """
    Processes the user's prompt

    Do's and dont's.

    """

    # exit Konsole
    if prompt == "exit":
        utils.exit_from_terminal()

    return prompt
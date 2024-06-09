# import global variables
import config

# import utilities
import utils.prompts as prompt

# import ai stuff
import utils.employees as chat

# Initialize global variables
config.RUNNING = True

def main():
    while config.RUNNING:
        # Prompt the user
        user_prompt = input(config.SHELL_NAME + ": ")
        proc_prompt = prompt.process_user_prompt(user_prompt)
        chat.ask_GPT(proc_prompt)

if __name__ == "__main__":
    main()
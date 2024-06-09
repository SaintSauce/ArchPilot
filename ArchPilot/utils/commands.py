import subprocess

def run_command(prompted_command: str):
    """
    Run a shell command and interact with it directly in the shell.

    Parameters:
    command (str): The command to be executed.
    
    """
    
    try:
        # Use Popen to run the command
        process = subprocess.Popen(prompted_command, shell=True)

        # Wait for the command to complete
        process.communicate()

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
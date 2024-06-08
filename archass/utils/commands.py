import subprocess

def run_command(command: str) -> str:
    """
    Execute a shell command and return its output.

    Parameters:
    command (str): The command to be executed.

    Returns:
    str: The stdout from the command if it executes successfully,
         otherwise the stderr from the command if an error occurs.

    Raises:
    subprocess.CalledProcessError: If the command execution fails.
    
    """

    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

# Example usage
if __name__ == "__main__":
    output = run_command("sudo pacman -Syu")
    print(output)
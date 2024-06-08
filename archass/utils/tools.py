import config

def terminate_program():
    """
    Sends a signal to exit the Konsole

    Probably just terminate main.

    """
    
    print("----------")
    print("Peace out!")
    print("----------")
    
    config.RUNNING = False
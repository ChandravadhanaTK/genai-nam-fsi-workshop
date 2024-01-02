# python module for all validations

def verify_choice(user_choice) -> int:
    """Verify the choice input by users

    Args:
        user_choice (string): user input 

    Returns:
        int: int value of choice, 
             in case of failure -1
    """
    try:
        i_val = int(user_choice)
        if i_val < 0 or i_val > 4:
            print("Please choose between 0 to 4!!")
            return -1
        return i_val
    except ValueError:
        print("Choice is invalid!!!")
        return -1


def verify_input(s: str) -> (int, bool):
    """Verify the input value

    Args:
        s (str): input value

    Returns:
        int : integer converted value of input
        bool: sucess or failure indicator
    """
    try:
        return int(s), True
    except ValueError:
        print("Input must be an integer")
        return 0, False

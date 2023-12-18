#Method 1
def is_palindrome(input_string: str):
    """Checks whether a string is palindrome or not using slicing

    Args:
        input_string (str): Input string
    """
    if input_string.lower() == input_string[::-1].lower():
        print(f"Yes, '{input_string}' is a palindrome string")
    else:
        print(f"No, '{input_string}' is NOT a palindrome string")

#Method 2
def is_palindrome_using_flag(input_string: str):
    """Checks whether a string is palindrome or not using flag and iterator

    Args:
        input_string (str): Input string
    """
    flag=0
    length=len(input_string)
    for i in range(0, length):
        if input_string[i].lower() != input_string[length-i-1].lower():
            flag=1
            break 
    if flag == 0:
        print(f"Yes, '{input_string}' is a palindrome string")
    else:
        print(f"No, '{input_string}' is NOT a palindrome string")

print("Welcome to Palindrome Checker...")
input_string = str(input("Enter your input string:")).strip()
#Calling Method 1 function is_palindrome
#is_palindrome(input_string)
#Calling Method 2 function is_palindrome_using_flag
is_palindrome_using_flag(input_string)
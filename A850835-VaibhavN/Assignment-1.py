# Palindrome Checker:
# Develop a program that checks whether a given string is a palindrome (reads the same forwards and backwards) 
# without using built-in reverse functions.


def Is_Palindrome(string: str):
    if string == string[::-1]:
        return print("String is a palindrome")
    else:
        return print("String is not a palindrome")


def Main():
    input_string = input("Enter string: ")

    # Check if string is empty
    if not(input_string and input_string.strip()):
        print("Please provide valid string input.")
    else:
        Is_Palindrome(input_string)

if __name__ == "__main__":
    Main()
    
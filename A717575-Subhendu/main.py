# the calculator app takes integer input from user
# and performs add, subtraction, multiplication and division

# create a class that takes 2 integer and performs the operation

# Flow:
#  Ask user to select the operation - provide choices 1 - 4, 0 - exit
#  ask user to enter the 2 integers
#  verify if the user input is integer or not
#  additional check for division to not allow 0
#  once operation completes, ask user if they want to perform another operation (run a loop)

from calculator import Calculator
from validations import verify_choice, verify_input


def main():
    """
    main function to get inputs from user and perform caclulations
    """
    text = """
------------------------------------
    Calculation App
    choices:
        1 - add
        2 - subtract
        3 - multiply
        4 - divide
        0 - exit
------------------------------------   
Please provide your selection: """
    first: bool = True
    while True:
        if not first:
            cont = input("Do you wish to continue (y/n): ")
            if cont.lower() != "y":
                print("Thank you for using calculator!")
                break
        first = False
        choice : str = input(text)
        choice: int = verify_choice(choice)
        if choice == -1:
            continue
        if choice == 0:
            print("Thank you for using calculator!")
            break
        a = input("Enter 1st number: ")
        a, valid = verify_input(a)
        if not valid:
            continue
        b = input("Enter 2nd number: ")
        b, valid = verify_input(b)
        if not valid:
            continue
        calc = Calculator(a, b)

        if choice == 1:
            print(f"{a}+{b}={calc.add()}")
        if choice == 2:
            print(f"{a}-{b}={calc.subtract()}")
        if choice == 3:
            print(f"{a}*{b}={calc.multiply()}")
        if choice == 4:
            if b == 0:
                print("2nd number can not be 0 for division")
                continue
            print(f"{a}/{b}={calc.divide()}")


if __name__ == "__main__":
    main()

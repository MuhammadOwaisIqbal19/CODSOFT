
                                               # MY CALCULATOR
def Addition(x,y):
    return x+y
def Subtraction(x,y):
    return x-y
def Multiplication(x,y):
    return x*y
def Division(x,y):
    return x/y

while True:
    try:
        choice = input(
            'Enter the Operation You want to perform:\n Press 1 for Addition \n Press 2 for Subtraction \n Press 3 for Multiplication \n Press 4 for Division \n ENTER HERE:')

        x = float(input("Enter the First Number in digits:"))
        y = float(input("Enter the Second Number in digits:"))

    except TypeError:
        print("Enter the Digit")


    try:
        if choice == "1":
            print('\n The Sum of two numbers is ', Addition(x, y))

        elif choice == "2":
            print('\n The Subtraction of two numbers is ', Subtraction(x, y))

        elif choice == "3":
            print('\n The Product of two numbers is ', Multiplication(x, y))
        elif choice == "4":
            print('\n The Division of two numbers is ', Division(x, y))
        else:
            print("\n INVALID OPERATION,ENTER +,-,*,% \n")
    except Exception as e:
        print("\n ENTER A DIGIT",e,"\n")
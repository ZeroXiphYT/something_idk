from termcolor import colored
#functions 


def add():
    num1 = input("Number 1\n")
    num2 = input("Number 2\n")
    z = int(num1)+int(num2)
    ans = print(colored(z, 'green'),"Is",num1,"+",num2)
def subtract():
    num1 = input("Number 1\n")
    num2 = input("Number 2\n")
    z = int(num1)-int(num2)
    ans = print(colored(z, 'green'),"Is",num1,"-",num2)
def multiply():
    num1 = input("Number 1\n")
    num2 = input("Number 2\n")
    z = int(num1)*int(num2)
    ans = print(colored(z, 'green'),"Is",num1,"x",num2)
def divide():
    num1 = input("Number 1\n")
    num2 = input("Number 2\n")
    z = int(num1)/int(num2)
    ans = print(colored(z, 'green'),"Is",num1,"÷",num2)
def rd():
    num1 = input("Number 1\n")
    num2 = input("Number 2\n")
    z = round(int(num1)/int(num2))
    ans = print(colored(z, 'green'),"Is",num1,"÷",num2)
 
    #calling and doing the functions
oper = input("Addition , Subtraction , Multiplication Or Division, use 'a' for addition 's' for subtraction, 'm' for multiplication and 'd' for division or 'rd' for rounded division\n")
if oper == "a":
    add()
else:
    if oper == "s":
        subtract()
    else:
        if oper == "m":
            multiply()
        else:
            if oper == "d":
                divide()
            else:
                if oper == 'rd':
                    rd()
                else:
                    input(colored('Invalid Operation', 'red'), 'Start It Again')
                
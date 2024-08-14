import math
def sum (a,b):
    c=a+b
    return c
def sub (a,b):
    c=a-b
    return c
def mul (a,b):
    c=a*b
    return c
def div (a,b):
    if (a>b):
        c=a/b
        return c
    else:
        print("a is less than b then we can not find the divide")
def rem (a,b):
    if (a>b):
        c=a%b
        return c
    else:
        print("a is less than b then we can not find the reminder")
def sqr (a):
    c=math.sqrt(a)
    return c
def root (a):
    c=math.sqrt(a)/0.5
    return c
def power (a,b):
    c=a**b
    return c
while True:
    print("Enter 1 for find the Addition of numbers")
    print("Enter 2 for find the Subtraction of numbers")
    print("Enter 3 for find the Multipaction of numbers")
    print("Enter 4 for find the Division of numbers")
    print("Enter 5 for find the Reminder of numbers")
    print("Enter 6 for find the Squre_root of numbers")
    print("Enter 7 for find the solution using by power of number")
    print("Enter 8 for Exit from the Program")

    choice=int(input("Enter your operation choice which you want to perform ._.!"))

    if(choice==1):
        x= int(input("enter the 1st num1"))
        y= int(input("enter the 2nd num2"))
        s=sum(x,y)
        print("ADDITION IS:",s)
    elif(choice==2):
        x=int(input("enter the 1st num"))
        y=int(input("enter the 2nd num"))
        s=sub(x,y)
        print("SUBSTRACTION IS :",s)
    elif(choice==3):
        x=int(input("enter the 1st num"))
        y=int(input("enter the 2nd num"))
        m=mul(x,y)
        print("MULTIPLY IS:",m)
    elif(choice==4):
        x=int(input("enter the 1st num"))
        y=int(input("enter the 2nd num"))
        d=div(x,y)
        print("DIVIDE IS:",d)
    elif(choice==5):
        x=int(input("enter the 1st num"))
        y=int(input("enter the 2nd num"))
        P=rem(x,y)
        print("REMINDER IS:",P)
    elif(choice==6):
        x=int(input("enter the num"))
        s=sqr(x)
        print("SQURE ROOT IS:",s)
    elif(choice==7):
        x=int(input("enter the 1st num"))
        y=int(input("enter the 2nd num"))
        d=power(x,y)
        print(f"THE POWER OF{a} IS TO BE {b} IS :")

    else:
        print("!<<--succesfully exit the calculator-->>!")
        break
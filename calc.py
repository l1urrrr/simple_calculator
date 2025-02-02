import time


def sum(n1,n2):
    return float(n1 + n2)

def subtract(n1,n2):
    return float(n1 + n2)

def prod(n1,n2):
    return float(n1 * n2)

def divide(n1,n2):
   return float(n1 / n2)

def exponent(n1,n2):
    return float(n1 ** n2)

def command():
    run = True
    while run :
        n1 = int(input("What's the first number?:"))
        time.sleep(0.3)
        print("+ \n - \n *\n / \n **")
        operation = int(input("Pick an operation:"))
        n2 = input("What's the next number ? :")
        ans = ""
        if operation == '+':
           ans = sum(n1,n2)
        elif operation == '-':
           ans =  subtract(n1,n2)
        elif operation == '*':
           ans = prod(n1,n2)
        elif operation == '/':
           ans = divide(n1,n2)
        elif operation == '**':
           ans = exponent(n1,n2)
        else:
            print("not valid!! Try again with one of the given operators. ")
        to_continue = input(f"Type'y' to continue calculating with {ans} or "
                           f"type "
                           f"'n' to start new calculation: ")
        if to_continue == 'y':
            continue
        else:
            break


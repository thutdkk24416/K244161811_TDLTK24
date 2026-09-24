# ax^2+bx+c=0
from math import sqrt

def quadratic(a,b,c):
    # print("Quadratic Equation Solving Program")
    # a = float(input("Enter a:"))
    # b = float(input("Enter b:"))
    # c = float(input("Enter c:"))
    if a == 0:
        # bx+c=0
        if b == 0 and c == 0:
            # print("Infinite solutions")
            return "Infinite solutions"
        elif b == 0 and c != 0:
            # print("No solutions")
            return "No solutions"
        else:
            x = -c / b
            # print("Solution x=", x)
            return x
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            # print("No solutions")
            return "No solutions"
        elif delta == 0:
            x = -b / (2 * a)
            # print("Double solutions x1=x2=", x)
            return x
        else:
            x1 = (-b - sqrt(delta)) / (2 * a)
            x2 = (-b + sqrt(delta)) / (2 * a)
            # print("x1=", x1)
            # print("x2=", x2)
            return x1, x2
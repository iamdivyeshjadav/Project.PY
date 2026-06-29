import math

def factorial_num():

    n = int(input("Enter Number : "))

    print("Factorial :", math.factorial(n))

def circle_area():

    r = float(input("Enter Radius : "))

    area = 3.14 * r * r

    print("Area :", area)

def trigono():

    a = float(input("Enter Angle : "))

    rad = math.radians(a)

    print("Sin :", math.sin(rad))
    print("Cos :", math.cos(rad))

def math_menu():

    while True:

        print("\n--- Math Menu ---")

        print("1. Factorial")
        print("2. Circle Area")
        print("3. Trigonometry")
        print("4. Back")

        ch = input("Enter Choice : ")

        match ch:

            case "1":
                factorial_num()

            case "2":
                circle_area()

            case "3":
                trigono()

            case "4":
                break

            case _:
                print("Wrong Input")
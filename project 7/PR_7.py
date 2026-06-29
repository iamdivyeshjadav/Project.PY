from modules.datetime_module import datetime_menu
from modules.math_module import math_menu
from modules.random_module import random_menu
from modules.uuid_module import create_uuid
from modules.file_module import file_menu

while True:

    print("\n======================")
    print(" Multi Utility Toolkit ")
    print("======================")

    print("1. Date and Time")
    print("2. Math Opration")
    print("3. Random Data")
    print("4. UUID Generate")
    print("5. File Opration")
    print("6. Exit")

    ch = input("Enter Choice : ")

    match ch:

        case "1":
            datetime_menu()

        case "2":
            math_menu()

        case "3":
            random_menu()

        case "4":
            print("UUID :", create_uuid())

        case "5":
            file_menu()

        case "6":
            print("Thank You ")
            break

        case _:
            print("Wrong Choice")
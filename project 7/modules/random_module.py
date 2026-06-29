import random
import string


def random_num():
    print("Random Number :", random.randint(1, 100))


def random_pass():
    l = int(input("Enter Password Length : "))

    data = string.ascii_letters + string.digits
    password = ""

    for i in range(l):
        password += random.choice(data)

    print("Password :", password)


def random_otp():
    otp = random.randint(1000, 9999)
    print("OTP :", otp)


def random_menu():
    while True:
        print("\n--- Random Menu ---")
        print("1. Random Number")
        print("2. Password Generate")
        print("3. OTP Generate")
        print("4. Back")

        ch = input("Enter Choice : ")

        match ch:
            case "1":
                random_num()
            case "2":
                random_pass()
            case "3":
                random_otp()
            case "4":
                break
            case _:
                print("Invalid Choice")
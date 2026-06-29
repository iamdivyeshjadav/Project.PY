from datetime import datetime
import time

def show_date():

    now = datetime.now()

    print("Current Date Time :", now)

def date_diff():

    d1 = input("Enter First Date (YYYY-MM-DD): ")
    d2 = input("Enter Second Date (YYYY-MM-DD): ")

    date1 = datetime.strptime(d1,"%Y-%m-%d")
    date2 = datetime.strptime(d2,"%Y-%m-%d")

    diff = abs((date2-date1).days)

    print("Total Days :", diff)

def stop_watch():

    input("Press Enter To Start:")

    start = time.time()

    input("Press Enter To Stop:")

    end = time.time()

    print("Time :", round(end-start,2),"sec")

def datetime_menu():

    while True:

        print("\n--- Date Time Menu ---")

        print("1. Current Date Time")
        print("2. Date Diffrence")
        print("3. Stop Watch")
        print("4. Back")

        ch = input("Enter Choice : ")

        match ch:

            case "1":
                show_date()

            case "2":
                date_diff()

            case "3":
                stop_watch()

            case "4":
                break

            case _:
                print("Invalid Choice")
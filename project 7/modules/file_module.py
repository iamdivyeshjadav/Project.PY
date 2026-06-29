def create_file():

    name = input("Enter File Name : ")

    file = open(name,"w")

    file.close()

    print("File Created")

def write_file():

    name = input("Enter File Name : ")

    data = input("Enter Data : ")

    file = open(name,"w")

    file.write(data)

    file.close()

    print("Data Saved")

def read_file():

    name = input("Enter File Name : ")

    file = open(name,"r")

    data = file.read()

    file.close()

    print("\nFile Data :")

    print(data)

def file_menu():

    while True:

        print("\n--- File Menu ---")

        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Back")

        ch = input("Enter Choice : ")

        match ch:

            case "1":
                create_file()

            case "2":
                write_file()

            case "3":
                read_file()

            case "4":
                break

            case _:
                print("Wrong Choice")
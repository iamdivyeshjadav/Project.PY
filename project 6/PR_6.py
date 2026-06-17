from datetime import datetime
class Journalmanager:
    def __init__(self):
        self.file_name = "journal.txt"
    def add_entry(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg = input("Enter Your Journal Entry: ")
        final_text = f"[{current_time}] {msg}\n"

        myfile = open(self.file_name, 'a')
        myfile.write(final_text)
        myfile.close()
        print("Entry saved successfully.")

    def show_all(self):
        try:
            myfile = open(self.file_name, 'r')
            print(myfile.read().strip())
            myfile.close()

        except FileNotFoundError:
            print("No journal entries found. Start by adding a new entry!")
    def search_word(self):
        s_word = input("Enter a keyword or date to search: ")

        is_found = False

        try:
            myfile = open(self.file_name, "r")

            for line in myfile:
                if s_word.lower() in line.lower():

                    if is_found == False:
                        print("\nMatching Entries:")
                        print("---------------------------------")
                        is_found = True

                    print(line.strip())

            myfile.close()

            if is_found == False:
                print("\nNo entries found for the keyword:", s_word + ".")

        except FileNotFoundError:
            print("\nNo journal entries found.")

    def clear_all(self):
        ans = input("Are you sure you want to delete all entries? (yes/no): ")

        if ans.lower() == "yes":
            myfile = open(self.file_name, 'w')
            myfile.write("")
            myfile.close()

            print("All journal entries have been deleted.")

        else:
            print("Delete operation cancelled.")


object = Journalmanager()

while True:

    print("\nWelcome To Personal Journal Manager")
    print("Please Select Option\n")

    print("press 1 for Add a New Entry")
    print("press 2 for View All Entries")
    print("press 3 for Search For Entry")
    print("press 4 for Delete All Entries")
    print("press 5 for Exit\n")

    c = input("Enter Your Choice: ")

    print()

    match c:

        case "1":
            object.add_entry()

        case "2":
            object.show_all()

        case "3":
            object.search_word()

        case "4":
            object.clear_all()

        case "5":
            print("Exiting Journal Manager...")
            break

        case _:
            print("Invalid Choice Entered ")
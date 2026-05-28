students_list = []
students_dict = {}
student_subjects= ["Math", "Science", "History", "English", "Art"]
print("welcome to the student data organizer")
while True:
    print("-------------------------------")
    print("please select an option:")
    print("press 1 for  add a student")
    print("press 2 for  display student data")
    print("press 3 for  update student data")
    print("press 4 for  delete student data")
    print("press 5 for  display subject offered")
    print("press 6 for  exit")
    choice = input("enter your choice: ")
    match choice:
        case "1":
            print("-------------------------------")
            student_ID = input("enter student ID: ")
            name = input("enter student name: ")
            age = input("enter student age: ")
            grade = input("enter student grade: ")
            date_of_birth = input("enter student date of birth (YYYY-MM-DD): ")
            subject = input("enter student subject (comma-separated): ")
            student_data = {"ID": student_ID, "name": name, "age": age, "grade": grade, "date_of_birth": date_of_birth, "subject": subject}
            students_list.append(student_data)
            students_dict[student_ID] = student_data
            print("student added successfully.")
        case "2":
            print("-------------------------------")
            for student in students_list:
                print(f"ID: {student['ID']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Date of Birth: {student['date_of_birth']}, Subject: {student['subject']}")
            if not students_list:
                print("no students found.")
        case "3":
            print("-------------------------------")
            student_ID = input("enter student ID to update: ")
            if student_ID in students_dict:
                name = input("enter new student name: ")
                age = input("enter new student age: ")
                grade = input("enter new student grade: ")
                date_of_birth = input("enter new student date of birth (YYYY-MM-DD): ")
                subject = input("enter new student subject (comma-separated): ")
                students_dict[student_ID] = {"ID": student_ID, "name": name, "age": age, "grade": grade, "date_of_birth": date_of_birth, "subject": subject}
                for i, student in enumerate(students_list):
                    if student["ID"] == student_ID:
                        students_list[i] = students_dict[student_ID]
                        print("student data updated successfully.")
                        break
            else:
                print("student ID not found.")
        case "4":
            print("-------------------------------")
            student_ID = input("enter student ID to delete: ")
            if student_ID in students_dict:
                del students_dict[student_ID]
                students_list = [student for student in students_list if student["ID"] != student_ID]
                print("student data deleted successfully.")
            else:
                print("student ID not found.")
        case "5":
            print("-------------------------------")
            print("subjects offered:")
            for subject in student_subjects:
                print(subject)
        case "6":
            print("thank you for using the student data organizer. goodbye!")
            break
        case _:
            print("invalid choice. please try again.")
"""
output:
welcome to the student data organizer
-------------------------------
please select an option:
press 1 for  add a student
press 2 for  display student data
press 3 for  update student data
press 4 for  delete student data
press 5 for  display subject offered
press 6 for  exit
enter your choice: 1
-------------------------------
enter student ID: 101
enter student name: divyesh
enter student age: 17
enter student grade: A
enter student date of birth (YYYY-MM-DD): 2000-12-08
enter student subject (comma-separated): Maths,Sci,Eng
student added successfully.
-------------------------------
please select an option:
press 1 for  add a student
press 2 for  display student data
press 3 for  update student data
press 4 for  delete student data
press 5 for  display subject offered
press 6 for  exit
enter your choice: 2
-------------------------------
ID: 101, Name: divyesh, Age: 17, Grade: A, Date of Birth: 2000-12-08, Subject: Maths,Sci,Eng
-------------------------------
please select an option:
press 1 for  add a student
press 2 for  display student data
press 3 for  update student data
press 4 for  delete student data
press 5 for  display subject offered
press 6 for  exit
enter your choice: 3
-------------------------------
enter student ID to update: 
student ID not found.
-------------------------------
please select an option:
press 1 for  add a student
press 2 for  display student data
press 3 for  update student data
press 4 for  delete student data
press 5 for  display subject offered
press 6 for  exit
enter your choice: 3
-------------------------------
enter student ID to update: 101
enter new student name: neev
enter new student age: 21
enter new student grade: A
enter new student date of birth (YYYY-MM-DD): 2005-12-01
enter new student subject (comma-separated): Maths,Eng
student data updated successfully.
-------------------------------
please select an option:
press 1 for  add a student
press 2 for  display student data
press 3 for  update student data
press 4 for  delete student data
press 5 for  display subject offered
press 6 for  exit
enter your choice: 4
-------------------------------
enter student ID to delete: 101
student data deleted successfully.
-------------------------------
please select an option:
press 1 for  add a student
press 2 for  display student data
press 3 for  update student data
press 4 for  delete student data
press 5 for  display subject offered
press 6 for  exit
enter your choice: 5
-------------------------------
subjects offered:
Math
Science
History
English
Art
-------------------------------
please select an option:
press 1 for  add a student
press 2 for  display student data
press 3 for  update student data
press 4 for  delete student data
press 5 for  display subject offered
press 6 for  exit
enter your choice: 6
thank you for using the student data organizer. goodbye!
"""
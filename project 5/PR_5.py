Employee_list = []
Manager_list = []
Developer_list = []

class Employee:
    def __init__(self, name=" ",age=0,salary=0,ID=0):
        self.name = None
        self.age = 0
        self.salary = 0
        self.ID = 0   
    def setter(self):
        self.name = input("\nName: ")
        self.age = int(input("Age: "))
        self.__id = int(input("ID: "))
        self.__salary = int(input("Salary: "))
    def display(self):
      print(f"\nName: {self.name} | Age: {self.age} | ID: {self.__id} | Salary: {self.__salary}")

class manager(Employee):
    def __init__(self):
        super().__init__()
        self.department = None
    def setter(self):
        super().setter()
        self.department = input("Department: ")
    def display(self):
        print(f"\nName: {self.name} | Age: {self.age} | ID: {self._Employee__id} | Salary: {self._Employee__salary} | Department: {self.department}")

class Developer(Employee):
    def __init__(self):
        super().__init__()
        self.language = None

    def setter(self):
        super().setter()
        self.language = input("Programming Language: ")
    def display(self):
        print(f"\nName: {self.name} | Age: {self.age} | ID: {self._Employee__id} | Salary: {self._Employee__salary} | Programming Language: {self.language}")

while True:
    print("\nEmployee Management System")
    print("Enter your choice:")
    print("press 1 for create an Employee")
    print("press 2 for create a manager")
    print("press 3 for create a developer")
    print("press 4 for show details")
    print("press 5 for exit")
    choice = input("Enter your choice: ")
    match choice:      
        case "1":
            e = Employee()
            e.setter()
            Employee_list.append(e)
        case "2":
            m = manager()
            m.setter()
            Manager_list.append(m)
        case "3":
            d = Developer()
            d.setter()
            Developer_list.append(d)
        case "4":
            while True:
              print("\n1. Display Employee")
              print("\n2. Display Manager")
              print("\n3. Display Developer")
              print("\n4. Exit")
              print("\nEmployee Details:")
              choose = int(input("Enter your choose: "))
              if choose == 1:
                for e in Employee_list:
                  e.display()
              elif choose == 2:
                for m in Manager_list:
                    m.display()
              elif choose == 3:
                for d in Developer_list:
                    d.display()
              elif choose == 4:
                  break
              else:
                print("Invalid choice. Please try again!!!")
        case "5":
            print("Exiting the program.")
            break
        case _:
            print("Invalid choice. Please try again!!!!")
    
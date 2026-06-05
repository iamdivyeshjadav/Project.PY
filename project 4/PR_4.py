print("welcome to the data analyzer and transformer program")
while True:
    print("*-----------------------------------------------*")
    print("please select an option:")
    print("press 1 for  input data")
    print("press 2 for Display data summary (built-in functions)")
    print("press 3 for Calculate factorial (recursaion)")
    print("press 4 for Filter data by a threshold (lambda function)")
    print("press 5 for Sort data")
    print("press 6 for  display dateset statistics (returning multiple values)")
    print("press 7 for  exit")
    choice = input("enter your choice: ")
    match choice:
        case "1":
            print("*-------------------------------*")
            data_input = list(map(int, input("Enter data for a 1D array (separated by spaces): ").split()))
            print(data_input)
            print("Data has been stored successfully.")
        case "2":
            print("*-------------------------------*")
            print("Data summary:")
            print("total elements:", len(data_input))
            print("minimum value:", min(data_input))
            print("maximum value:", max(data_input))
            print("sum of all values:", sum(data_input))
            print("average value:", sum(data_input) / len(data_input))
        case "3":
            print("*-------------------------------*")
            n = int(input("Enter a number to calculate its factorial: "))
            def factorial(n):
                if n == 0:
                    return 1
                else:
                    return n * factorial(n-1)
            print("The factorial of", n, "is", factorial(n))
        case "4":
            print("*-------------------------------*")
            threshold = int(input("Enter a threshold value to filter data: "))
            filtered_data = list(filter(lambda x: x > threshold, data_input))
            print("Filtered data:", filtered_data)
        case "5":
            print("*-------------------------------*")
            print("Sorting options:")   
            print("1. Ascending order")
            print("2. Descending order")
            choice_sort = input("Enter Your Choice: ")
            match choice_sort:
                case "1":
                    sorted_data = sorted(data_input)
                    print("Data sorted in ascending order:", sorted_data)
                case "2":
                    sorted_data = sorted(data_input, reverse=True)
                    print("Data sorted in descending order:", sorted_data)
                case _:
                    print("Invalid sorting choice. Please try again.")
        case "6":
            print("*-------------------------------*")
            def dataset_statistics(data):
                total = len(data)
                minimum = min(data)
                maximum = max(data)
                average = sum(data) / total
                return total, minimum, maximum, average
            total, minimum, maximum, average = dataset_statistics(data_input)
            print("Dataset statistics:")
            print("Total elements:", total)
            print("Minimum value:", minimum)
            print("Maximum value:", maximum)
            print("Average value:", average)
        case "7":
            print("thank you for using the program! Goodbye!")
            break
        case _:
            print("Invalid choice. Please try again.")
'''
'''

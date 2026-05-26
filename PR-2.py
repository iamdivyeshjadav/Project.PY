while True: 
    print("welcome to the pattern generator and number analyzer!\n") 
    print("Please select an option:") 
    print("1. Pattern Generator") 
    print("2. Number Analyzer") 
    print("3. Exit") 
    a = int(input("enter your choice (1, 2, or 3): ")) 
    match a: 
        case 1: 
            print("press 1 for left aligned triangle") 
            print("press 2 for right aligned triangle") 
            print("press 3 for diamond pattern") 
            pattern=int(input("enter the pattern you want to generate (1, 2, or 3): ")) 
            match pattern: 
                case 1: 
                    n=int(input("enter the number of rows for the left aligned triangle: ")) 
                    for i in range(1,n+1): 
                        print("*"*i) 
                case 2: 
                    n = int(input("enter the number of rows for the right aligned triangle: ")) 
                    for i in range(1,n+1): 
                        print(" "*(n-i)+"*"*i) 
                case 3: 
                    n = int(input("enter the number of rows for the diamond: ")) 
                    for i in range(1, n + 1): 
                        print(" "*(n-i)+"*"*(2*i-1)) 
                    for i in range(n-1,0,-1): 
                        print(" "*(n-i)+"*"*(2*i-1)) 
                case _: 
                    print("invalid pattern choice, please try again") 
                    continue                
        case 2: 
            print("you have selected number analyzer") 
            num1 = int(input("enter a number to analyze: ")) 
            num2 = int(input("enter another number to analyze: "))
            for i in range(num1,num2+1): 
                if i%2==0: 
                    print(i, "is an even number") 
                else: 
                    print(i, "is an odd number")     
            total_sum = 0 
            for i in range(num1,num2+1): 
                total_sum += i 
            print("the sum of the numbers from",num1,"to",num2,"is",total_sum) 
        case 3: 
            print("you have selected exit") 
            print("thank you for using the program!") 
            break 
        case _: 
            print("invalid choice, please try again")
            continue
"""
output:
welcome to the pattern generator and number analyzer!

Please select an option:
1. Pattern Generator
2. Number Analyzer
3. Exit
enter your choice (1, 2, or 3): 1
press 1 for left aligned triangle
press 2 for right aligned triangle
press 3 for diamond pattern
enter the pattern you want to generate (1, 2, or 3): 3
enter the number of rows for the diamond: 5
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
welcome to the pattern generator and number analyzer!

Please select an option:
1. Pattern Generator
2. Number Analyzer
3. Exit
enter your choice (1, 2, or 3): 2
you have selected number analyzer
enter a number to analyze: 10
enter another number to analyze: 15                  
10 is an even number
11 is an odd number
12 is an even number
13 is an odd number
14 is an even number
15 is an odd number
the sum of the numbers from 10 to 15 is 75
welcome to the pattern generator and number analyzer!

Please select an option:
1. Pattern Generator
2. Number Analyzer
3. Exit
enter your choice (1, 2, or 3): 3
you have selected exit
thank you for using the program!
"""

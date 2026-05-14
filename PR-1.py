print("welcome to the interactive personal data collector! ","\n")
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in cm: "))
weight = float(input("Please enter your weight in kg: "))
favorite_place = input("Please enter your favorite place: ")
favorite_number = input("Please enter your favorite number: ")
favorite_food = input("Please enter your favorite food: ")
favorite_ipl_team = input("Please enter your favorite IPL team: ")
hobbies = input("Please enter your hobbies : ")
print("Thank you for providing your information! Here is what we have collected:","\n")
print("Name: ", name,"type: ", type(name), "memory address: ", id(name))
print("Age: ", age,"type: ", type(age), "memory address: ", id(age))
print("Height: ", height, "cm", "type: ", type(height), "memory address: ", id(height))
print("Weight: ", weight, "kg", "type: ", type(weight), "memory address: ", id(weight))
print("Favorite Place: ", favorite_place,"type: ", type(favorite_place), "memory address: ", id(favorite_place))
print("Favorite Number: ", favorite_number,"type: ", type(favorite_number), "memory address: ", id(favorite_number))
print("Favorite Food: ", favorite_food,"type: ", type(favorite_food), "memory address: ", id(favorite_food))
print("Hobbies: ", hobbies,"type: ", type(hobbies), "memory address: ", id(hobbies))
print("Favorite IPL Team: ", favorite_ipl_team,"type: ", type(favorite_ipl_team), "memory address: ", id(favorite_ipl_team))
print("Your birth year is: ", 2025 - int(age)," based on your agre of ", age,"\n")
print("thank you for using the interactive personal data collector! Have a great day!")
'''
output:
welcome to the interactive personal data collector! 
Please enter your name: neev
Please enter your age: 18
Please enter your height in cm: 1.80
Please enter your weight in kg: 75
Please enter your favorite place: Gurukul       
Please enter your favorite number: 77
Please enter your favorite food: pizza
Please enter your favorite IPL team: GT
Please enter your hobbies : Skydiving
Thank you for providing your information! Here is what we have collected:
Name:  neev type:  <class 'str'> memory address:  2006822627552
Age:  18 type:  <class 'int'> memory address:  2006822627600
Height:  1.8 cm type:  <class 'float'> memory address:  2006822627648
Weight:  75.0 kg type:  <class 'float'> memory address:  2006822627696
Favorite Place:  Gurukul type:  <class 'str'> memory address:  2006822627744
Favorite Number:  77 type:  <class 'int'> memory address:  2006822627792
Favorite Food:  pizza type:  <class 'str'> memory address:  2006822627840
Hobbies:  Skydiving type:  <class 'str'> memory address:  2006822682096
Favorite IPL Team:  GT type:  <class 'str'> memory address:  2006822627888
Your birth year is:  2007  based on your agre of  18
thank you for using the interactive personal data collector! Have a great day!
'''

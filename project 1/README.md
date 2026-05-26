# Interactive Personal Data Collector

This Python script (`PR-1.py`) is an interactive program designed to collect, process, and display personal information from a user. It demonstrates basic Python concepts including user input, data type conversion, memory management (using `id()`), and simple arithmetic.

## Features
- **Interactive Prompts:** Collects a wide range of data such as name, age, physical attributes, and personal preferences [cite: 1].
- **Data Type Identification:** Uses the `type()` function to show how Python categorizes different inputs [cite: 1].
- **Memory Address Retrieval:** Uses the `id()` function to display the unique memory address of each variable [cite: 1].
- **Automated Calculation:** Calculates the user's birth year based on the provided age and the reference year 2025 [cite: 1].

## How to Run
1. Ensure Python is installed on your system.
2. Execute the script via the terminal:
   ```bash
   python PR-1.py
   ```

## Sample Output
Based on the provided script, here is an example of the interaction:
```
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
```

# Q1. Write a program that asks the user for their name and age, then prints a
# sentence like:
# Hello Shradha, you are 21 years old!

name = input("enter name: ")
age = input("enter age: ")
print("Hello",name, "you are",age, "years old")

# Q2. Take two numbers as input from the user and print their sum, difference,
# product, and quotient.

a = int(input("enter a: "))
b = int(input("enter b: "))
print("sum: ", a + b)
print("diff: ", a - b)
print("prod: ", a * b)
print("quot: ", a / b)

# Q3. Ask the user to enter two integers and one float. Convert them all to floats
# and print their average.

num1 = float(input("enter num1: "))
num2 = float(input("enter num2: "))
num3 = float(input("enter num3: "))
avg = (num1 + num2 + num3) / 3
print("avg: ",avg)

# Q4. The user enters a string containing a number (e.g.,"45" ). Convert it to:
# • an integer
# • a float
# • a string again
# Print all three values with their types.

user = input("enter str: ")
num = int(user)
decimal = float(user)
string = str(user)
print(num, type(num))
print(decimal, type(decimal))
print(string, type(string))

# Q5. Evaluate and print the result of the following expression:
            # x = 10 + 3 * 2 ** 2
# Based on what you learnt in the lecture explain why the output is what it is.

x = 10 + 3 * 2 ** 2
print("x: ",x)

# Q6. Write a program to swap values of two numbers entered by the user.

n1 = int(input("enter first num: "))
n2 = int(input("enter second num: "))
n1 , n2 = n2 , n1
print("first num" , n1)
print("second num", n2)

# Q7. Ask the user for a temperature in Celsius (string input). Convert it to ,
# then calculate and print temperature in Fahrenheit.
# Conversion formula: FahrenheitTemp = (CelsiusTemp ∗ (9/5)) + 32

celsius_temp = input("enter temp: ")
fahrenheit_temp = float(celsius_temp) * (9/5) + 32
print("temperature in Fahrenheit: ", fahrenheit_temp)

# Q8. Take the radius (r) as user input and print the area.
# Use the formula: Area = π * r2 (value of π = 3.14)

rad = float(input("enter radius: "))
PI = 3.14
Area = PI * rad * rad
print("Area of cirle: ",Area)

# Q9. Ask the user for: Principal (P), Rate (R), Time (T). Convert all to and
# compute simple interest:
            # SI = (P ∗ R ∗ T)/100

principal = float(input("enter P: "))
rate = float(input("enter R: "))
time = float(input("enter T: "))
SI = (principal * rate * time) / 100
print("Simple Interest: ",SI)

# Q10. Take a decimal number as input (like: 45.78 ) and output its:
# • integer part - 45
# • fractional part - .78

dec_num = float(input("enter number: "))
integer_part = int(dec_num)
fractional_part = dec_num - integer_part
print("integer part: ", integer_part)
print("fractional part: ", fractional_part )






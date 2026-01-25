# Q1. Write a program that takes as input. Using conditional statements,
# calculate the finaltax rate based on these rules:
# • If salary < 30,000 → 5%
# • If salary is 30,000–70,000 → 15%
# • If salary > 70,000 → 25%

salary = int(input("Enter salary: "))

if salary < 30000:
    tax_rate = 5
elif salary <= 70000:
    tax_rate = 15
else:
    tax_rate = 25

tax_amount = salary * tax_rate / 100
final_salary = salary - tax_amount

print("Tax rate:", tax_rate, "%")
print("Tax amount:", tax_amount)
print("Final salary after tax:", final_salary)

# Q2. Write a function that takes two integers and a and b prints all even
# numbers between them (inclusive).

def even_num(a , b):
    for i in range(a, b+1):
        if i%2 == 0:
            print(i)
even_num(1, 10)

# Q3. Write a function that prints the digits of a number, .n
# For eg:n = 312 , there are 3 digits in it 3, 1 and 2 & we need to print them.

def print_digits(num):
    for digit in str(num):
        print(digit)

print_digits(312)

# Q4. Write a function to return the count the number of digits in a number, .

def count_digits(n):
    n = abs(n)   # negative number handle
    if n == 0:
        return 1

    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

print(count_digits(512))

#Q5. Write a function to return the sum of digits of a number, n.

def cal_sum(n):
    n = abs(n)   # for negative numbers
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

n = int(input("Enter n: "))
print("Sum of digits =", cal_sum(n))

#Q6. Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.

for i in range(1 , 101):
    if(i%3 == 0 and i%5 == 0):
        print(i)

# Q7. Design a program to continuously input a number from user & print if it is
# positive or negative until the user enters “Quit

while True:
    user = input("Enter a number or type Quit to stop: ")

    if user == "quit":
        print("Program stopped.")
        break

    num = int(user)

    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero (Neither positive nor negative)")

# Q8. Letʼs create a Simple Calculator that performs arithmetic operations. Create
# a function calculator(a, b, operation) that performs addition, subtraction,
# multiplication, or division based on the operation parameter.
# [ operation parameter can have values ‘+’,‘-’ ,'*’ & ‘/’.

def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b  
    else:
        return "Invalid operation"

print(calculator(12, 6, '/'))
    
# Q9. Write a function is_prime(n) that returns True if is a 
# prime number and False otherwise, using a loop.
 
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(7))

# Q10. Letʼs create a “NumberGuessing Game”. Given a secret number (already
# decided by you), write a program that asks the user to guess it and prints:
# • "Too high" if the guess is above the number
# • "Too low" if the guess is below
# • "Correct!" if the guess matches

num = 10

while True:
    user = int(input("Guess the number: "))

    if user > num:
        print("Too high")
    elif user < num:
        print("Too low")
    else:
        print("Correct!")
        break










  
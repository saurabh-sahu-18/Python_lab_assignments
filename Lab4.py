#Q.1 Declare a div() function with two parameters. Then call the function and pass two
# numbers and display their division.

def div(a,b):
    print("division is : ",a/b)

number1 = int(input("enter 1st number"))
number2 = int(input("enter 2nd number"))
div(number1,number2)

#=======================================================================================================================================================================================================================================
#Q.2 Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number .

def square(a):
    print("square is : ",a*a)

number1 = int(input("enter a number : "))
square(number1)

#=======================================================================================================================================================================================================================================
#Q.3 Using max() and min() functions display the maximum and minimum of 5 random numbers.

import random

# generating random numbers from 1 to 100
random_numbers = [random.randint(1,100) for i in range(5)]
print("The random numbers are: ",random_numbers)

max_number = max(random_numbers)
min_number = min(random_numbers)

print("maximum number is: ",max_number)
print("minimum number is: ",min_number)

#=======================================================================================================================================================================================================================================
#Q.4 Accept a name from the user and display that in lower case using lower() function

def lower(a):
    print("Your name in lower case: ",a.lower())

name = input("enter your name in upper case: ")
lower(name)

#=======================================================================================================================================================================================================================================
# Q.5 Write a lambda function that takes one argument and returns 'Positive' if the number is
# greater than 0, 'Negative' if it's less than 0, and 'Zero' if it's 0. Test it with different
# numbers

# Defining lambda function
check_sign = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

# Test the lambda function with different numbers
print(check_sign(10))  
print(check_sign(-5))  
print(check_sign(0))

#=======================================================================================================================================================================================================================================
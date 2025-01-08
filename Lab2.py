#Q1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd
number = int(input("enter any number : "))
result = "even" if number % 2 == 0 else "odd" #checking even/odd
print("The selected number is : ",result)


#Q2.Using input function take two number and then swap the number
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print(f"Data Before swapping: number1 = {number1}, number2 = {number2}")

number1, number2 = number2, number1 # Swapping the numbers
print(f"Data After swapping: number1 = {number1}, number2 = {number2}")


#Q3.Write a Program to Convert Kilometers to Miles
kilometers = float(input("enter value in kilometers : "))
miles = kilometers*0.621371 #converting to miles
print("The value in miles is : ",miles)

#Q4.Find the Simple Interest on Rs. 200 for 5 years at 5% per year.

#taking inputs from the user:
principal_amount = float(input("enter amount : "))
time_period = float(input("enter time period : "))
rate_of_interest = float(input("enter rate of interest : "))

simple_interest = (principal_amount*time_period*rate_of_interest)/100 #calculating simple interest
print(f"The simple interest of Rs{principal_amount} is : Rs{simple_interest:.2f}")



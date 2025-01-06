#1. Calculate the multiplication and sum of two numbers 
num1 = int(input("enter 1st number:"))
num2 = int(input("enter 2nd number:"))

multiple = num1 * num2
add = num1 + num2

print("multiplication of the 2 numbers is : " , multiple)
print("sum of the 2 numbers is : " , add)

#2. Declare two variables and print that which variable is largest using ternary operators 
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

greatest = num1 if num1>num2 else num2
print("The greatest of 2 numbers is", greatest)

#3. Python program to convert the temperature in degree centigrade to Fahrenheit
celcius = float(input("enter temperature in celcius: "))

farenheit = (celcius * 9/5) + 32
print("Temperature in farenheit of ",celcius, "is", farenheit)

#4. Python program to find the area of a triangle whose sides are given
import math

a = int(input("enter side a : "))
b = int(input("enter side b : "))
c = int(input("enter side c : "))

s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The area of the triangle is", area)



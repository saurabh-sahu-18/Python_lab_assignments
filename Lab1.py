#1. Calculate the multiplication and sum of two numbers 
number1 = int(input("enter 1st number:"))
number2 = int(input("enter 2nd number:"))

multiple = number1 * number2
add = number1 + number2

print("multiplication of the 2 numbers is : " , multiple)
print("sum of the 2 numbers is : " , add)

#2. Declare two variables and print that which variable is largest using ternary operators 
number1 = int(input("Enter the 1st number: "))
number2 = int(input("Enter the 2nd number: "))

greatest = number1 if number1>number2 else number2
print("The greatest of 2 numbers is", greatest)

#3. Python program to convert the temperature in degree centigrade to Fahrenheit
celcius = float(input("enter temperature in celcius: "))

farenheit = (celcius * 9/5) + 32
print("Temperature in farenheit of ",celcius, "is : ", farenheit)

#4. Python program to find the area of a triangle whose sides are given
import math

side_a = int(input("enter side a : "))
side_b = int(input("enter side b : "))
side_c = int(input("enter side c : "))

semi_perimeter = (side_a + side_b + side_c)/2
area = math.sqrt(semi_perimeter*(semi_perimeter-side_a)*(semi_perimeter-side_b)*(semi_perimeter-side_c))
print("The area of the triangle is : ", area)



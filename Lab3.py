#Q.1 Python program to check leap year
year = int(input("Enter a year: "))

#Checking leap year condition
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
#=======================================================================================================================================================================================================================================

#Q.2 Python Program to Find the Largest Among Three Numbers
number1 = int(input("enter 1st number : "))
number2 = int(input("enter 2nd number : "))
number3 = int(input("enter 3rd number : "))

# Finding the largest number
if number1 >= number2 and number1 >= number3:
    largest = number1
elif number2 >= number1 and number2 >= number3:
    largest = number2
else:
    largest = number3

print("The largest number is : ", largest)
#=======================================================================================================================================================================================================================================

#Q3.Python Program to Check if a Number is Positive, Negative or 0
number = int(input("enter your number : "))

#checking number is positive,negative or 0
if number > 0:
    print("the number is positive")
elif number < 0:
    print("the number is negative")
else:
    print("the number is 0")
#=======================================================================================================================================================================================================================================

"""Q.4 A toy vendor supplies three types of toys: Battery Based Toys, Key-based
Toys, and Electrical Charging Based Toys. The vendor gives a discount of
10% on orders for battery-based toys if the order is for more than Rs. 1000.
On orders of more than Rs. 100 for key-based toys, a discount of 5% is
given, and a discount of 10% is given on orders for electrical charging based
toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3
are used for battery based toys, key-based toys, and electrical charging based
toys respectively. Write a program that reads the product code and the order
amount and prints out the net amount that the customer is required to pay
after the discount."""

#Taking product code & amount from user
print("Refer these Product codes : battery toy-1/key toy-2/electric toy-3")
product_code = int(input("enter your product code : "))

#checking for valid product code
if product_code < 1 or product_code > 3:
    print("invalid product code entered.")

amount = int(input("enter your purchase amount : "))

#checking for discount and printing final value
if product_code == 1:
    if amount >= 1000:
        print("your payable amount is : Rs", amount - (amount*10/100))
    else :
        print("your payable amount is : Rs", amount)
elif product_code == 2:
    if amount >= 100:
        print("your payable amount is : Rs", amount - (amount*5/100))
    else :
        print("your payable amount is : Rs", amount)
elif product_code == 3:
    if amount >= 500:
        print("your payable amount is : Rs", amount - (amount*10/100))
    else :
        print("your payable amount is : Rs", amount)
#=======================================================================================================================================================================================================================================

"""5. A transport company charges the fare according to following table:
WAP in python to get distance from user and calculate payable amount according to given data

Distance             Charges
1-50                 8Rs./Km
51-100               10Rs./Km
> 100                12Rs/Km"""

#taking data from user
distance = int(input("enter distance travelled : "))

#checking valid distance entered
if distance < 1:
    print("invalid distance entered")

if distance >= 1 and distance <= 50:
    print("your payable amount is : Rs",8*distance)
elif distance >= 51 and distance <= 100:
    print("your payable amount is : Rs",10*distance)
elif distance > 100:
    print("your payable amount is : Rs",12*distance)

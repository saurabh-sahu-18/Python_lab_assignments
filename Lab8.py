#=======================================================================================================================================================================================================================================
#Q.1 Write a Python program to Count all letters, digits, and special symbols from the given string Input = “P@#yn26at^&i5ve” Output: Chars = 8 Digits = 2 Symbol = 3

def count_characters(input_string):
    chars = digits = symbols = 0  # Initialize counters for each category

    # Iterate through each character in the string
    for char in input_string:
        if char.isalpha():  # Check if the character is a letter
            chars += 1
        elif char.isdigit():  # Check if the character is a digit
            digits += 1
        else:  # Otherwise, it's a symbol
            symbols += 1

    print(f"Chars = {chars}")
    print(f"Digits = {digits}")
    print(f"Symbol = {symbols}")

# Given string
input_string = "P@#yn26at^&i5ve"
count_characters(input_string)

#=======================================================================================================================================================================================================================================
#Q.2 Write a Python program to remove duplicate characters of a given string. Input = “String and String Function” Output: String and Function

def remove_duplicates(input_string):
    result = ""  # Initialize an empty string to store the result
    seen = set()  # Set to keep track of characters already encountered

    # Iterate through each character in the string
    for char in input_string:
        if char not in seen:  # If character hasn't been encountered
            result += char  # Add it to the result
            seen.add(char)  # Add the character to the 'seen' set

    return result

# Given string
input_string = "String and String Function"
output_string = remove_duplicates(input_string)
print("Output:", output_string)

#=======================================================================================================================================================================================================================================
#Q.3 Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN” Output: UpperCase : 5 LowerCase : 18 NumberCase : 5 SpecialCase : 11

def count_characters(input_string):
    upper_case = lower_case = numbers = special_case = 0  

    # Iterate through each character in the string
    for char in input_string:
        if char.isupper():  
            upper_case += 1
        elif char.islower():  
            lower_case += 1
        elif char.isdigit():  
            numbers += 1
        else: 
            special_case += 1

    print(f"UpperCase : {upper_case}")
    print(f"LowerCase : {lower_case}")
    print(f"NumberCase : {numbers}")
    print(f"SpecialCase : {special_case}")

input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
count_characters(input_string)

#=======================================================================================================================================================================================================================================
#Q.4 Write a Python Count vowels in a string input= “Welcome to Python Assignment” Output: Total vowels are: 8

def count_vowels(input_string):
    vowels = "aeiouAEIOU"  # Define vowels (both lowercase and uppercase)
    vowel_count = sum(1 for char in input_string if char in vowels)  # Count vowels

    print(f"Total vowels are: {vowel_count}")

input_string = "Welcome to Python Assignment"
count_vowels(input_string)

#=======================================================================================================================================================================================================================================

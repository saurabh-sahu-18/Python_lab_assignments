#=======================================================================================================================================================================================================================================
#Q.1 Write a Python program to sum all the items in a list. 

def sum_of_list(numbers):
    total = 0
    for num in numbers:  
        total += num
    return total

num_list = [10, 20, 30, 40, 50]
print("Sum of list elements:", sum_of_list(num_list))

#=======================================================================================================================================================================================================================================
#Q.2 Write a Python program to get the largest and smallest number from a list without builtin functions. 

def find_largest_smallest(numbers):
    # Initialize smallest and largest with the first element of the list
    smallest = largest = numbers[0]

    # Iterate through the list
    for num in numbers:
        if num < smallest:  
            smallest = num
        if num > largest:  
            largest = num

    return smallest, largest

num_list = [10, 25, 5, 78, 3, 90, 45]

smallest, largest = find_largest_smallest(num_list)

print("Smallest number:", smallest)
print("Largest number:", largest)

#=======================================================================================================================================================================================================================================
#Q.3 Write a Python program to find duplicate values from a list and display those. 

def find_duplicates(numbers):
    duplicates = []  
    seen = set()  

    for num in numbers:
        if num in seen and num not in duplicates:
            duplicates.append(num)  # Add to duplicates if seen before
        else:
            seen.add(num)  # Add to seen set if first occurrence

    return duplicates

num_list = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 1]

duplicate_values = find_duplicates(num_list)
print("Duplicate values:", duplicate_values)

#=======================================================================================================================================================================================================================================
#Q.4 Write a Python program to split a given list into two parts where the length of the first part of the list is given. 

# Original list: 
# [1, 1, 2, 3, 4, 4, 5, 1] 
# Length of the first part of the list: 3 
# Splitted the said list into two parts: 
# ([1, 1, 2], [3, 4, 4, 5, 1]) 

def split_list(original_list, first_part_length):
    # Slice the list into two parts
    first_part = original_list[:first_part_length]
    second_part = original_list[first_part_length:]
    
    return first_part, second_part

original_list = [1, 1, 2, 3, 4, 4, 5, 1]

first_part_length = 3

first_part, second_part = split_list(original_list, first_part_length)

print("Splitted the said list into two parts:", (first_part, second_part))

#=======================================================================================================================================================================================================================================
#Q.5 Write a Python program to traverse a given list in reverse order, and print the elements with the original index. 

# Original list:
# ['red', 'green', 'white', 'black'] 
# Traverse the said list in reverse order:
# black  
# white
# green
# red

def traverse_reverse(original_list):
    # Loop through the list in reverse using index
    for i in range(len(original_list) - 1, -1, -1):
        print(original_list[i])  

original_list = ['red', 'green', 'white', 'black']

traverse_reverse(original_list)

#=======================================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================================
#Q1. Write a Python program to count the occurrences of each word in a given sentence string = “To change the overall look of your document. To change the look available in the gallery” 

from collections import Counter

string = "To change the overall look of your document. To change the look available in the gallery"

# Convert to lowercase and remove punctuation
string = string.lower().replace(".", "")

# Split the string into words
words = string.split()

# Count word occurrences
word_count = Counter(words)

# Display the result
for word, count in word_count.items():
    print(f"{word}: {count}")

#=======================================================================================================================================================================================================================================
#Q.2 Write a Python program to remove a newline in Python String = "\nBest \nDeeptech \nPython \nTraining\n" 

string = "\nBest \nDeeptech \nPython \nTraining\n"
newString = string.replace("\n", "")

print(newString)

#=======================================================================================================================================================================================================================================
#Q.3 Write a Python program to reverse words in a string String = “Deeptech Python Training” 

def reverse_words(sentence):
    words = sentence.split()  # Split the string into words
    reversed_sentence = " ".join(reversed(words))  # Reverse the list and join it back
    return reversed_sentence

string = "Deeptech Python Training"
result = reverse_words(string)

print("Reversed Words:", result)

#=======================================================================================================================================================================================================================================
#Q.4 Write a Python program to count and display the vowels of a given text String=”Welcome to python Training”

def count_vowels(text):
    vowels = "aeiouAEIOU"  # List of vowels (both uppercase and lowercase)
    vowel_list = [char for char in text if char in vowels]  # Extract vowels
    vowel_count = len(vowel_list)  # Count vowels

    print(f"Vowels in the string: {' '.join(vowel_list)}")  # Display vowels
    print(f"Total number of vowels: {vowel_count}")  # Display count

string = "Welcome to python Training"
count_vowels(string)

#=======================================================================================================================================================================================================================================
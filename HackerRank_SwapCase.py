"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
Function Description

Complete the swap_case function in the editor below.

swap_case has the following parameters:

string s: the string to modify
Returns

string: the modified string
Input Format

A single line containing a string .

Constraints


Sample Input 0

HackerRank.com presents "Pythonist 2".
Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""

# Successfull Code def swap_case(s):
def swap_case(s):
    # Most "Pythonic" solution
    # return s.swapcase()
    
    # Manual Solution below if Python did not have s.swapcase()

    # Strings are immutable, so we'll build a new string
    # An empty list is efficient for appending characters, then join at the end. 
    result_chars = []
    
    # Goal: Prepare an mutable structure to build the new string
    # Process: Initialize an empty list 'result_chars'
    # Rationale: Appendign to a list is efficient. Concatenating strings repeatedly ('resule_string += char') in a loop is inefficient because it creates a new string object each time. Building a list of characters and then 'join'ing them once at the end is the standard efficient way to build strings
    
    
    # Though Process: Iterate through each character of the input string
    for char in s:
    # Though Process:
    # Goal: Process each character of the input string individually
    # Process: Use a 'for..in' loop to iterate directly over the string 's'
    # Rationale: Python strings are iterable, making this the next direct way to access each character
    
        # Thought Process: Check if the character is a letter
        # If is's lowercase letter, convert to uppercase
        # If it's uppercase convert to lowercase
        # Otherwise, keep as is
        if char.islower():
            # Identify is the character is lowercase letter
            # Process: Use the string method 'char.islower()'
            # Rationale: This is a built-in character method that efficiently checks if a character is a lowercase letter. It correctly handles various Unicode lowercase letters
            
            result_chars.append(char.upper())
            # Goal: Convert the lowercase characters to uppercase
            # Process: Use the string method 'char.upper()'
            # Rationale: This is the standard way to convert a character (or string) to its uppercase equivalent
        
        elif char.isupper():
            # Goal: Identify if the character is an uppercase letter
            #Process: Use the string method 'char.isupper()'
            # Rationale: Similar to 'islower()', this robustly checks for uppercase letters, including unicode
            
            result_chars.append(char.lower())
            # Goal: Convert the uppercase character to lowercase
            # Process: Use the string method 'char.lower()'
            # Rationale: Standard way to convert to lowercase
        
        else:
            # IF not upper or lower, its's non-alphabetic. Keep as is
            result_chars.append(char)
            # Goal: Include non-aplphabetic characters unchanged
            # Process: Simply append the original character
            # Rationale: Adheres to the problem statement's requirement to preserve other characters
    
    # Join the list of characters back into a single string
    return "".join(result_chars)
    # Goal: Combine all processed characters into the final result string
    # Process: Use '"".join(iterable)'. The empty string '""' acts as the separator (no separator in this case)
    # Rationale: This is the most efficient and Pythonic way to concateneate elements from an iterable (like our list of characters) into a single string
        

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
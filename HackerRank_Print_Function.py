The included code stub will read an integer, , from STDIN.

Without using any string methods, try to print the following:

123...n

Note that "" represents the consecutive values in between.

Example

n = 5

Print the string 12345.

Input Format

The first line contains an integer .

Constraints

1 <= n <= 150

Output Format

Print the list of integers from  through  as a string, without spaces.

Sample Input 0

3
Sample Output 0

123

if __name__ == '__main__':
    n = int(input())

# Create an empty list to store the string representation of numbers

number_strings = []

# Loop from 1 to n (inclusive)

for i in range(1, n + 1):
    # Convert the integer to a string using buil-in str() function
    # append the string to our list
    
    number_strings.append(str(i))
    
# Print all the collected strings without spaces
# *number_strings unpacks all the list into individual arguments for print()
# sep: '' tells print() to use an empty string as a seperator between arguments
    
print(*number_strings, sep='')
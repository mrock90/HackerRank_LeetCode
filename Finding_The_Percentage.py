# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# Example

# marks key:value pairs are:

# 'alpha': [20,30,40]
# 'beta': [30, 50, 70]
# query_name = 'beta'

# The query_name is 'beta'. beta's average score is .

# Input Format

# The first line contains the integer , the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

# Constraints
# 2 <= n <= 10
# 0 <= marks[i] <= 100
# length of marks = 3

# Output Format

# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

# Sample Input 0

# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# Sample Output 0

# 56.00
# Explanation 0

# Marks for Malika are  whose average is 

# Sample Input 1

# 2
# Harsh 25 26.5 28
# Anurag 26 28 30
# Harsh
# Sample Output 1

# 26.50

# Successfull code solving problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # Step 1: Retieve the list of marks for the queried student
    # We access the the dictionary using the query_name as the key
    marks = student_marks[query_name]
    
    # Step 2: Calculate the sum of the marks
    # The sum() built-in function is efficient for this
    total_marks = sum(marks)
    
    # Step 3: Calculate the average
    # The len() built-in function gives us the count of marks
    average_marks = total_marks / len(marks)
    
    # Step 4: Print the average , formatted to 2 decimal places
    # An f-string with :.2 is the pythonic way to format 2 decimal places
    print(f"{average_marks:.2f}")
if __name__ == '__main__':
    # Step 1: Initialize an empty list to hold all student data
    # Each element in this list will be another list: [name, score]
    students_data = []
    
    # Read the total number of students from the the first line of input
    num_students = int(input())
    
    # Loop 'num_students' times to read each student's name and score
    for _ in range(num_students):
        name = input() # Read the students name (string)
        score = float(input()) # Read the students score and converts to a floating-point number
        
        # Add the current students [name, score] pair as a sub-list to our main list
        students_data.append([name, score])
        
        # At this point, 'students_data' will look something like this:
        # [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akrita', 41], ['Harsh', 39]]
        
    # Step 2: Find the second-lowest grade
    # First, we'll extract all all the scores in a single list
    # We will use list comprehension for a concise and Pythonic way to achieve this
    # Equivalent to:
    # scores = []
    # for student in student.data:
    #   scores.append(student[1]) # Student 1 is the score
    scores = [student[1] for student in students_data]
        
    # Now to find the secpnd lowest *unique* grade:
    # Convert the list of scores to a set to automatically remove dupicate grades
    # Then convert it back to a list so we can sort it
    unique_sorted_scores = sorted(list(set(scores)))
        
    # The second lowest grade will be at index 1 of this sorted list of unique sco
    # (Index 0 is the lowest score, Index 1 is the second lowest score)
    second_lowest_grade_value = unique_sorted_scores[1]
        
    # Step 3: Collect names of students who have the second lowest grade
    names_with_second_lowest_grade = []
    for student in students_data:
        # Check if the current student's score matches our identified second lowest grade
        if student[1] == second_lowest_grade_value:
            # If it matches, add their name to the collections list
            names_with_second_lowest_grade.append(student[0]) # student[0] os the name
        
    # Step 4: Sort these names alphabetically
    # The problem requires alphabetical order if multiple students share the same grade
    names_with_second_lowest_grade.sort()
        
    # Step 5: Print each name on a new line
    # Iterate through the sorted list on names and print each one:
    for name in names_with_second_lowest_grade:
        print(name)
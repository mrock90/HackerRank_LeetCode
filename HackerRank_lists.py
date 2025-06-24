if __name__ == '__main__':
    # 1. Initialize our list. This will store the integers we manipulate.
    # We use a standard Python lis, which is highly flexible and efficient for these operations
    arr = []
    
    # 2. Read the number of commands (N).
    # Input() reads a line as a string , int() converts the string to an integer
    N = int(input())
    
    # 3. Iterate through each command
    # We loop N times, once for each command we expect.
    for _ in range(N):
        # 4. Read the current command line
        # Example: "insert 0 5" or "print"
        command_line = input()
        
        # 5. Split the command line into parts
        # This nreaks the string into a list of strings based on spaces
        # Example; "insert 0 5" becomes ['insert', '0', '5']
        # Example: "print" becomes ['print']
        parts = command_line.split()
        
        # 6. Extract the command name (the first part)
        # This will be 'insert', 'print', 'remove', etc
        command_name = parts[0]
        
        # 7. Use conditional statements (if/elif/else) to execute the correct operation
        # This is a classic pattern for dipactching actions based on input
        
        if command_name == 'insert':
            # For 'insert', we expect two arguments: postions (i) and element (e)
            # These are ar parts [1] and parts [2] respectively
            # Crucially, we conver them to integers using int() becasue list.insert() expects integers
            # This directly uses the list's built-in insert() method, which is Pythonic
            arr.insert(int(parts[1]), int(parts[2]))
            
        elif command_name == 'print':
            # For 'print', we simply print the current state of the list
            # Python's print() funtion automatically formats lists nicely
            print(arr)
            
        elif command_name == 'remove':
            # For 'remove', we expect one argument: the element (e) to remove
            # We convert it to an integer. list.remove() removes the first occurence
            # Direct use of list.remove() is Pythonic
            arr.remove(int(parts[1]))
        
        elif command_name == 'append':
            # For 'append', we expect one argument: the element (e) to add
            # We convert it to an integer. list.append() adds to the end
            # Direct use of list.append is Pythonic
            arr.append(int(parts[1]))
            
        elif command_name == 'sort':
            # For 'sort', there are no arguments
            # list.sort() sorts the list in-place (modifies the original list) in ascending order
            # This is the most efficient and Pythonic way to sort a list if you don't need a new one
            arr.sort()
            
        elif command_name == 'pop':
            # For 'pop', ther are no arguments
            # list.pop removes and returns the last element. We don't need the returned valued here
            # Direct use of list.pop() is Pythonic
            arr.pop()
            
        elif command_name == 'reverse':
            # For 'reverse', there are no arguments 
            # list.reverse() reverses the list in-place (modifies the original list)
            # Direct use of list.reverse() is Pythonic
            arr.reverse()
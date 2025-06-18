# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


class Solution:
    def isValid(self, s: str) -> bool:
        # Step 1: Initialize an empty list to act as a stack
        # In Python, list's append() and pop() methods make it perfect for stack operations
        stack = []

        # Step 2: Create mapping of closing brackets to thier corresponsing opening brackets
        # This dictionary allows us to quickly find the expected opening brakcet for any clsoing bracket
        bracket_map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        # Step 3: Iterate through each character in the inpur string "s"
        for char in s:
            # Check if current character is a closing bracket
            if char in bracket_map:
                # If its a closing bracket:

                # Sub-step 3a: Check for unmatched closing bracket 
                # If stack is empty, it means we found a closing bracket
                # but there's no open bracket on the stack to match it with
                # E.g., s = "])"
                if not stack:
                    return False
                
                # Sub-step 3b: Check for type and order match
                # Get the expected opening bracket for the current closing character from our map
                expected_open = bracket_map[char]
                # Pop the top element from the stack. This is the most recently opened bracket
                actual_open = stack.pop()

                # Compare the popped element (actual_open) eith the expected_open.
                # If they dont match, it means the brackets are either of different types or are not in correct closing order (e.g., s = "([)]")
                if actual_open != expected_open:
                    return False
            # If current character is an opening bracket 
            # (Since the constraints guarantee s only contains brackets, if its not a closing one, it must be an open one)
            else:
                # Push the opening bracket onto the stack
                # We do this to remember that this bracket is currently "open" and is awaiting its corresponding closing bracket.
                stack.append(char)
        # Step 4: After interating through the entire string, perform the final check
        # If the stack is empty, it means every opening bracket encountered was successfully matched and popped by a corresponding closing bracket. The string is valid
        # If stack is NOT empty, it means there are still unmatched opening brackets left.
        # E.g., s = "([{"
        return not stack # 'mot stack' returns True is stack is empty, False otherwise
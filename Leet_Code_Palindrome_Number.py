Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Edge Cases
        # 1. Negative numbers are not palindromes. (e.g., -121 -> 121-)
        # 2. Numbers ending in 0 (except for 0 itself) are not palindromes.
        #    (e.g., 10 -> 01, 120 -> 021)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Build the reversed number
        reverted_number = 0
        while x > reverted_number: # This condition stops when we've processed about half the digits
            digit = x % 10
            reverted_number = reverted_number * 10 + digit
            x //= 10 # Integer division to remove the last digit from x

        # After the loop, we have two possibilities for a palindrome:
        # 1. The number has an even number of digits: x and reverted_number will be equal.
        #    Example: x = 1221 -> x becomes 12, reverted_number becomes 12
        # 2. The number has an odd number of digits: x will be the middle digit,
        #    and reverted_number will have one more digit (the middle digit at its end).
        #    So, we need to remove the last digit from reverted_number.
        #    Example: x = 121 -> x becomes 1, reverted_number becomes 12.
        #    Here, 1 == (12 // 10) which is 1.
        return x == reverted_number or x == reverted_number // 10
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].



class Solution:
    def romanToInt(self, s: str) -> int:
        # Step 1 : Map Roman Numerals to Integer Value
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        
        # Step 2: Initialize Variables for Consideration
        total = 0
        
        """ This will store the value of the Roman Numeral character to the right """
        prev_value = 0
        
        # Step 3: Iterate from Right-to-Left
        """ len(s) -1 is the indexc of the last character """
        """ -1 is the stop value (so it includes index 0) """
        """ -1 is the step value (decrement by 1 each time) """
        for i in range(len(s) -1, -1, -1):
            
            # Step 4: Get Current Symbols Value
            current_symbol = s[i]
            current_value = roman_map[current_symbol]

            # Step 5: Apply Subtaction/Addicion Logic
            """
            If current value is less than previous value (from right to left), 
            it's a subtraction case
            """
            """
            Example: For 'IV', when processing 'I' (1), prev_value is 5. Since 1 < 5, subtract
            """
            """
            Example: For 'VI', when processing 'V' (5), prev_value is 1. 
            Since 5 is NOT < 1,add 
            """
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value

            # Step 6: Update Previous Value for the next iteration to the left
            prev_value = current_value
        
        # Step 7: Return the Final total
        return total
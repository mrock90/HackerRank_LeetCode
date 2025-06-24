class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Thought Process:
        # The problem asks for the "first occurence" of a substring ('needle) within a larger string ('haystack')
        # It also sepcifies that if the substring is not found, we should return -1
        # My first thought immediately goes to Python's rich set of built-in string methods 
        # Rationale: 
        # Pytho's 'str.find()' method is desinged precisely for this task
        # - It takes a substring as an argument
        # - It returns the lowest (first) index in the string where the substring is found
        # Crucially, if the substring is not found, it returns -1

        # This behavior perfectly matches all the requirements of the problem statement
        # Using a built-in method like 'find()' is highly recommended in Python for serveral reasons:
        # 1. Efficiency: These methods are typically implemented in C and are heavily optimized for performance, ofter utilizing highly efficient algorithms (like a variation of Boyer-Moore or Rabin-Karp). This makes them much faster than most custom Python implementations for this problem, especially for large strings.
        # 2. Readability: The code is concise and self-explanatory. 'haystack.find(needle)' clearly states its intent
        # 3. Robustness: Built-in methods handle edge cases (like 'needle' being longer than 'haystack', or 'needle' being empty if allowed by constraints) reliably without explicit checks in my code
        # Therefore, the simplest and most Pythonic soulution is to directly use 'haystack.find(needle)' 
        return haystack.find(needle)
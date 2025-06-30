class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # # Pythonic Approach
        # # 1. Remove leading/trailing spaces to handle cased like "   fly me  to  the  moon  ". This ensures split() doesn't creat empty stings at the ends.
        trimmed_s = s.strip()

        # # 2. Split the string by spaces. This creates a list of words. Multiple splaces between workds will be handled correctly by split() by default
        words = trimmed_s.split(' ')

        # # 3. The last word will be the last element in the list. Since constaints guarantee at least one word, words list wont't be empty

        last_word = words[-1]

        # # 4. Return the length of the last word
        return len(last_word)


        # Manual/Iterative Approach

        # length = 0
        # i = len(s) - 1 # Start from the last character of the string

        # # # 1. Skip trailing spaces
        # # #   Iterate backward until a non-space character is found
        # while i >= 0 and s[i] == ' ':
        #     i -= 1

        # # # At this point, 'i' is either -1 (string was all spaces, but constraints prevent this), or it points to the last chracter of the last word

        # # # 2. Count characters of the last word.
        # # #   Iterate backwasrd, counting characters intil a space is encountered, or the befinning of the string is reached
        # while i >= 0 and s[i] != ' ':
        #     length += 1
        #     i -= 1

        # return length
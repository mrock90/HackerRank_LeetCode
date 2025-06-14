Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.


from typing import List # Required for the type hint List[str]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Step 1: Handle initial edge cases

        # Rationale: If the list of strings is empty, there's no prefix to find.
        # Importance: Handles a common edge case gracefully and prevents errors.
        if not strs:
            return ""

        # Rationale: If there's only one string, that string itself is the common prefix.
        # Importance: Simplifies the logic for this specific, simple case.
        if len(strs) == 1:
            return strs[0]

        # Step 2: Choose a reference string and initialize prefix
        # We'll use the first string as our reference to compare against others.
        longest_common_prefix = ""
        reference_string = strs[0] # Example: "flower"

        # Step 3: Outer Loop - Iterate character by character through the reference string
        # Rationale: The common prefix cannot be longer than the first string.
        # 'char_idx' will represent the current character's position.
        for char_idx in range(len(reference_string)):
            current_char = reference_string[char_idx] # Example: 'f', then 'l', then 'o', etc.

            # Step 4: Inner Loop - Compare 'current_char' across all other strings
            # Rationale: Iterate through the rest of the strings (starting from the second one, index 1).
            # This is where we verify if the 'current_char' is common to *all* strings.
            for str_idx in range(1, len(strs)):
                other_string = strs[str_idx] # Example: "flow", then "flight"

                # Check 4a: Handle cases where 'other_string' is shorter than the current char_idx
                # Rationale: If any string is shorter than the current character index,
                #            we've gone beyond its length, so no further common prefix is possible.
                # Importance: Prevents IndexError and correctly terminates the search early.
                if char_idx >= len(other_string):
                    return longest_common_prefix # Return whatever common prefix we've built so far.

                # Check 4b: Check for character mismatch
                # Rationale: If the character at 'char_idx' in 'other_string' does not match
                #            the 'current_char' from our 'reference_string'.
                # Importance: This is the core mismatch detection. If found, the prefix ends here.
                if other_string[char_idx] != current_char:
                    return longest_common_prefix # Return the prefix found up to the previous character.

            # Step 5: If the inner loop completes, it means 'current_char' matched in all strings.
            # Rationale: The 'current_char' is indeed common to all strings up to this point.
            # Importance: Builds the longest common prefix incrementally.
            longest_common_prefix += current_char

        # Step 6: If the outer loop finishes, it means the entire reference string
        #         is a common prefix to all other strings.
        # Rationale: All characters of the reference string were common prefixes.
        # Importance: Returns the final result in cases where the first string is the common prefix itself.
        return longest_common_prefix
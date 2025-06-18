# Instructions for Problem 
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

# Successful Code:

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge Cases: Handle an empty input array
        # If there are no elements, there are no unique elements, so k is 0
        if not nums:
            return 0
        
        # Initialize the "write-pointer"
        # This pointer indicates the posiion where the next unique value will be written
        # We start it at 1 because num[0] (the first element) is always consideted unique
        # (as there's nothing before it to be a duplicate of)
        write_pointer = 1

        # Iterate with the "read-pointer" from the second element (index 1) to the end of the array
        # The "read-pointer" traverses all elements to check for uniqueness
        for read_pointer in range(1, len(nums)):
            # Core Logic: Compare the element at "read-pointer" with its immediate predecessor
            # Since the array is sorted, duplicates are alwaus adjacent
            if nums[read_pointer] != nums[read_pointer - 1]:
                # If they are different, we have found a unique element
                # We "write" this unique element to the position indicated by "write=pointer"
                # This effectively moves unique elements to the front of the array
                nums[write_pointer] =nums[read_pointer]

                # Increments "write_pointer" to prepare foe the next unique element
                write_pointer += 1

        # After the loop finishes, "write_pointer" holds the count for the next element
        # This is "k" as per the problem description
        # The array "nums" will have the first "write_pointer" elements filled with the unique values
        # preserving their original relative order
        return write_pointer
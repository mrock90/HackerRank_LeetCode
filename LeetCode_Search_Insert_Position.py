class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Finds the index of the target in sorted array. If the target is not found, it returns the index where it would be if it were inserted in order.

        This function uses on iterative binary search algorithm to achieve 0(log n) runtime.

        Args:
            nums: A sorted list of distinct integers.
            target: The integer value to search for or find the insertion point.

        Returns:
            The index of the target if found, otherwise the index where it would be inserted in order.
        """
        # Initialize two pointers, 'left' and 'right', to define the current search space.
        # 'left' starts at the beginnig fo teh array (index 0)
        # 'right' starts at the end of the array (last index)
        left, right = 0, len(nums) - 1

        # The binary search loop continues as long as the 'left' pointer is less than or equal to 'right' pointer. This means there's still a valid search space (even if it's just one element)
        while left <= right:
            # Calculate the middle index
            # Using (left + (right - left) // 2 is robust afainst potential integer overflow

            mid = left + (right - left) // 2

            # Three possible comparison outcomes:
            # Case 1: The middle element is exactly the target
            if nums[mid] == target:
                return mid
            
            # Case 2: The middle element is less than the target
            # This means the target, if it exists, must be in the right half.
            # So, we shift our 'left' pointet to 'mid - 1' to search exclusively in the right subarray
            elif nums[mid] < target:
                left = mid + 1

            # Case 3: The middle element is greater than the target. 
            # This means the target, it it exists, must be in the left half.
            # So, we shift our 'right' pointer the 'mid - 1' to seach exclusively in the left subarray
            else: # nums[mid] > target
                right = mid - 1
        
        # If the loop finishes, the target was not found.
        # At this point, 'left' represenets the correct insertion point

        # Rationale for 'left' being the insertion point:
        # The loop terminates when 'left > right'
        # - If target ' is greater than all elements, 'left' will increment past 'len(nums) - 1' and become 'len(nums)'. This is the correct insertion index at the end
        # - If 'target is smaller than all elements. 'right' eill become - 1, and 'left' will remain 0. This is the correct insertion index at the beginning.
        # - If 'target' is between two elements, 'left' will advance to the index of the first element that is greater than 'target'. This is where 'target' should be inserted

        return left
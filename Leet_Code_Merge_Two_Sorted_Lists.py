# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted singly-linked lists into a single sorted list.

        Args:
            list1 (Optional[ListNode]): The head of the first sorted linked list.
            list2 (Optional[ListNode]): The head of the second sorted linked list.

        Returns:
            Optional[ListNode]: The head of the merged sorted linked list.
        """
        # Initialize a dummy head node. This makes handling the first node of the merged list easier.
        # We will eventually return dummy_head.next.
        dummy_head = ListNode()
        # Initialize a 'current' pointer to traverse and build the merged list.
        current = dummy_head

        # Traverse both lists as long as both have nodes.
        # We compare the values of the current nodes from list1 and list2.
        while list1 is not None and list2 is not None:
            # If the current node in list1 has a value less than or equal to
            # the current node in list2.
            if list1.val <= list2.val:
                # Attach list1's current node to the merged list.
                current.next = list1
                # Move the list1 pointer to its next node.
                list1 = list1.next
            else:
                # Otherwise (list2's current node has a smaller value).
                # Attach list2's current node to the merged list.
                current.next = list2
                # Move the list2 pointer to its next node.
                list2 = list2.next

            # Always advance the 'current' pointer in the merged list.
            # It now points to the node that was just added.
            current = current.next

        # After the loop, one of the lists might still have remaining nodes.
        # Since these remaining nodes are already sorted, we can simply
        # append the rest of that list to the end of our merged list.
        if list1 is not None:
            current.next = list1
        elif list2 is not None:
            current.next = list2

        # The actual merged list starts from the node after the dummy_head.
        return dummy_head.next
    

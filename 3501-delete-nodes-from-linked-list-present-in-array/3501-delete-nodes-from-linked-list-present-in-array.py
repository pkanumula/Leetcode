# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Convert nums to a set for O(1) lookups
        num_set = set(nums)
        
        # Create a dummy node to simplify edge cases (like removing the head)
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Traverse the list
        while current and current.next:
            if current.next.val in num_set:
                # Skip the node with a value in num_set
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        
        # Return the new head (dummy.next)
        return dummy.next

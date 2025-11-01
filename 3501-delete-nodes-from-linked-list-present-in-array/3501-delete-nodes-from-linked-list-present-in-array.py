# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert nums to a set for O(1) lookup
        remove_set = set(nums)
        
        # Create a dummy node to handle cases where head itself needs removal
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize pointers
        prev, curr = dummy, head
        
        # Traverse the linked list
        while curr:
            if curr.val in remove_set:
                # Skip the node if its value is in nums
                prev.next = curr.next
            else:
                # Move prev pointer only if node not removed
                prev = curr
            curr = curr.next
        
        # Return new head
        return dummy.next

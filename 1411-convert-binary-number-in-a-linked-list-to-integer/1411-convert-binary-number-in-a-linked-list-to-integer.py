# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = 0
        current = head
        while current:
            # shift left by 1 (multiply by 2) and add the current bit
            num = (num << 1) | current.val
            current = current.next
        return num

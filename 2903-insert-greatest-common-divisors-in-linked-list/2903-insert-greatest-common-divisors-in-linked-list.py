# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def gcd(self, a, b):
        # Implementing GCD using the Euclidean algorithm
        while b:
            a, b = b, a % b
        return a
    
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        
        while current and current.next:
            # Calculate the GCD of current node and next node
            gcd_value = self.gcd(current.val, current.next.val)
            
            # Create a new node with the GCD value
            gcd_node = ListNode(gcd_value)
            
            # Insert the new node between current and current.next
            gcd_node.next = current.next
            current.next = gcd_node
            
            # Move to the next pair (skip the newly inserted node)
            current = gcd_node.next
            
        return head

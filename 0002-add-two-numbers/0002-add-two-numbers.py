class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)  # Dummy node to simplify handling the head
        current = dummy  # Pointer to build the new list
        carry = 0  # Initialize carry to 0
        
        while l1 or l2 or carry:
            # Get the values of the current nodes; if no node, use 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and the new carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # Create a new node with the digit and append it to the result list
            current.next = ListNode(digit)
            current = current.next
            
            # Move to the next nodes in l1 and l2 if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next

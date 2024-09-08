class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        # Step 1: Determine the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Step 2: Calculate the size of each part
        part_size = length // k
        extra_nodes = length % k
        
        # Step 3: Split the linked list into parts
        result = []
        current = head
        
        for i in range(k):
            part_head = current
            part_length = part_size + (1 if i < extra_nodes else 0)
            
            # Move the current pointer to the end of the current part
            for j in range(part_length - 1):
                if current:
                    current = current.next
            
            # Break the link to create the end of the current part
            if current:
                next_part = current.next
                current.next = None
                current = next_part
            
            result.append(part_head)
        
        # Step 4: If there are fewer nodes than k, add None to the result
        while len(result) < k:
            result.append(None)
        
        return result

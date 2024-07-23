import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        
        # Create a min-heap
        heap = []
        
        # Add the first node of each list to the heap
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))
        
        # Create a dummy head for the result list
        dummy = ListNode()
        current = dummy
        
        while heap:
            # Extract the smallest node from the heap
            val, i, node = heapq.heappop(heap)
            current.next = ListNode(val)
            current = current.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        return dummy.next

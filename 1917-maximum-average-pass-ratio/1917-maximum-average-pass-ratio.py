import heapq

class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        # Function to calculate the gain in pass ratio if we add one student
        def gain(passed, total):
            return (passed + 1) / (total + 1) - passed / total
        
        # Create a max heap based on the gain
        max_heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(max_heap)
        
        # Distribute the extra students to maximize the pass ratio
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-gain(p + 1, t + 1), p + 1, t + 1))
        
        # Calculate the final average pass ratio
        return sum(p / t for _, p, t in max_heap) / len(classes)
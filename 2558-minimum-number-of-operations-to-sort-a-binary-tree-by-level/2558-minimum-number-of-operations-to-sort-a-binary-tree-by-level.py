from collections import deque

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def min_swaps_to_sort(arr):
            n = len(arr)
            indexed_arr = [(value, index) for index, value in enumerate(arr)]
            indexed_arr.sort()
            visited = [False] * n
            swaps = 0

            for i in range(n):
                if visited[i] or indexed_arr[i][1] == i:
                    continue

                cycle_size = 0
                j = i

                while not visited[j]:
                    visited[j] = True
                    j = indexed_arr[j][1]
                    cycle_size += 1

                if cycle_size > 1:
                    swaps += cycle_size - 1

            return swaps

        if not root:
            return 0

        queue = deque([root])
        total_operations = 0

        while queue:
            level_size = len(queue)
            level_values = []

            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            total_operations += min_swaps_to_sort(level_values)

        return total_operations

from collections import deque

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])
        level = 0

        while queue:
            size = len(queue)
            current_level = []

            for _ in range(size):
                node = queue.popleft()
                if level % 2 == 1:
                    current_level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level % 2 == 1:
                # Reverse values of nodes in the current level
                values = [node.val for node in current_level][::-1]
                for i, node in enumerate(current_level):
                    node.val = values[i]

            level += 1

        return root

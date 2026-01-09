# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> tuple[int, Optional[TreeNode]]:
            if not node:
                return 0, None

            ld, lnode = dfs(node.left)
            rd, rnode = dfs(node.right)

            if ld == rd:
                return ld + 1, node
            elif ld > rd:
                return ld + 1, lnode
            else:
                return rd + 1, rnode

        return dfs(root)[1]

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, depth):
            if not node:
                return (None, depth)
            left_lca, left_depth = dfs(node.left, depth + 1)
            right_lca, right_depth = dfs(node.right, depth + 1)
            
            if left_depth == right_depth:
                return (node, left_depth)
            elif left_depth > right_depth:
                return (left_lca, left_depth)
            else:
                return (right_lca, right_depth)
        
        lca, _ = dfs(root, 0)
        return lca

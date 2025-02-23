# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        post_index = {val: i for i, val in enumerate(postorder)}
        self.pre_index = 0
        
        def build(l: int, r: int) -> Optional[TreeNode]:
            root = TreeNode(preorder[self.pre_index])
            self.pre_index += 1
            if l == r:
                return root
            idx = post_index[preorder[self.pre_index]]
            root.left = build(l, idx)
            if idx < r - 1:
                root.right = build(idx + 1, r - 1)
            return root
        
        return build(0, len(postorder) - 1)

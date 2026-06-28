# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth1 = self.recurr(root.left)
        depth2 = self.recurr(root.right)

        if depth1 > depth2:
            return depth1
        else:
            return depth2
    
    def recurr(self, root):
        if not root:
            return 1
        depth1 = self.recurr(root.left)
        depth2 = self.recurr(root.right)

        if depth1 > depth2:
            return 1 + depth1
        else:
            return 1 + depth2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (not p and q):
            return False
        if p.val == q.val:
            return self.sameHelper(p.left, q.left) and self.sameHelper(p.right, q.right)
        else:
            return False
    
    def sameHelper(self, p, q):
        if not p and not q:
            return True
        if (p and not q) or (not p and q):
            return False
        if p.val == q.val:
            return self.sameHelper(p.left, q.left) and self.sameHelper(p.right, q.right)
        else:
            return False

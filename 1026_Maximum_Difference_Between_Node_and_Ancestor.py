# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/"""
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = 0
        paths = {}
        stack = [(root, [root.val, root.val])] # root, min, max
        
        while len(stack) > 0:
            n, v = stack.pop(0)
            result = max(result, v[1]-v[0])
            if n.left:
                stack.append((n.left, [min(n.left.val, v[0]), max(n.left.val, v[1])]))
            if n.right:
                stack.append((n.right, [min(n.right.val, v[0]), max(n.right.val, v[1])]))
            
        return result
      
    # TODO: recursive
        

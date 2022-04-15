# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """https://leetcode.com/problems/count-complete-tree-nodes/"""
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        stack = [root]
        lvl = 0
        while len(stack) > 0:
            new_stack = []
            for n in stack:
                if n.left:
                    new_stack.append(n.left)
                if n.right:
                    new_stack.append(n.right)
            
            lvl += 1
            if len(new_stack) < 2**lvl:
                return 2**(lvl+1) -1 - 2**lvl + len(new_stack)
            stack = new_stack

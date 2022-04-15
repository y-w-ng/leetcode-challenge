# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """https://leetcode.com/problems/count-good-nodes-in-binary-tree/"""
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        result = 1
        stack = [(root, root.val)]
        
        while len(stack) > 0:
            
            node, v = stack.pop(0)
            if node.left:
                if node.left.val >= v:
                    result += 1
                stack.append((node.left, max(node.left.val, v)))
            if node.right:
                if node.right.val >= v:
                    result += 1
                stack.append((node.right, max(node.right.val, v)))
                
        return result
    
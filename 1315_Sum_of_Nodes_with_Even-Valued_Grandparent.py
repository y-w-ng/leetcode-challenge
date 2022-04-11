# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total = 0
        if root and root.val % 2 == 0:
             gc = self.has_grandchilds(root)
             for n in gc:
                total += n.val
        if root.left:
            total += self.sumEvenGrandparent(root.left)
        if root.right:
            total += self.sumEvenGrandparent(root.right)
                
        return total
        
        
    def has_grandchilds(self, root):
        if root:
            parents = [n for n in [root.left, root.right] if n]
            grandchilds = [child for n in parents for child in [n.left, n.right] if child]
            return grandchilds
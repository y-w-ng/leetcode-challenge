# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def __init__(self):
        self.leaves = [0, 0] # sum, level of the leave node


    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:    
        self.dfs(root, 0)
        return self.leaves[0]

    def dfs(self, root, lvl):
        if root is None:
            return
        lvl += 1
        if root.left is None and root.right is None:

            if lvl > self.leaves[1]:
                self.leaves = [root.val, lvl]
            elif lvl == self.leaves[1]:
                self.leaves = [self.leaves[0]+root.val, lvl]

        if root.left:
            self.dfs(root.left, lvl)
        if root.right:
            self.dfs(root.right, lvl)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # using a member variable and a nested funtion
        # if you don't initialize it as a member variable, use the nonlocal
        # keyword before you update it inside the nested function 
        self.res = 0

        # retruns height 
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            # nonlocal res
            # res = ...
            self.res = max(self.res, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.res
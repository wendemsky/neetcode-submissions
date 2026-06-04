# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # dfs to find the start node in the tree
        # use the "same tree" problem to check subtree exists
        target = subRoot.val
        subRootStart = None
        stack = [root]
        res = False
        while stack:
            node = stack.pop()
            if node.val == target:
                res = self.sameTree(node, subRoot)
                if res == True:
                    break
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


    def sameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
        
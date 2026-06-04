# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            # check the structure
            if not p and not q:
                return True
            elif (not p and q) or (p and not q):
                return False
            # (p and q) meaning the structure is the same
            else:
                # check the value
                if p.val != q.val:
                    return False

            print(f"p.val = {p.val} \n q.val = {q.val}")

            # check left and right, return true only if both are true else return false
            return dfs(p.left, q.left) and dfs(p.right, q.right)

        return dfs(p, q)
            
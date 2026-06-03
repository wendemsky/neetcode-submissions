# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # bfs
        if not root:
            return
        queue = deque([root])
        while queue:
            node = queue.popleft()

            tmp = node.left
            node.left = node.right
            node.right = tmp

            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return root
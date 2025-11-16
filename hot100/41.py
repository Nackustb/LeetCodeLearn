from collections import deque
class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        return self.bfs(root)

    def bfs(self, root):
        res = []
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res
     
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Example usage:
# Constructing a binary tree:
#         3
#        / \
#       9  20
#          /  \
#         15   7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
solution = Solution()
print(solution.levelOrder(root))  # Output: [[3], [9, 20], [15, 7]]

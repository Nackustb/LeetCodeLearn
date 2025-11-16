from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                # 每层最后一个节点
                if i == level_size - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res

        # res = []
        
        # def dfs(node, depth):
        #     if not node:
        #         return
        #     if depth == len(res):
        #         res.append(node.val)
        #     dfs(node.right, depth + 1)
        #     dfs(node.left, depth + 1)
        
        # dfs(root, 0)
        # return res
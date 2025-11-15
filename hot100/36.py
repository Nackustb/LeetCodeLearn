from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)      
            res.append(node.val) 
            dfs(node.right)     
        
        dfs(root)
        return res
    
# example usage:
root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
sol = Solution()
print(sol.inorderTraversal(root))  # Output: [1, 3, 2]
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        # if not root:
        #     return
        
        # self.flatten(root.left)
        # self.flatten(root.right)

        # right = root.right
        
        # root.right = root.left
        # root.left = None
        
        # cur = root
        # while cur.right:
        #     cur = cur.right
        
        # cur.right = right

        while root:
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                
                pre.right = root.right

                root.right = root.left
                root.left = None

            root = root.right 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False
                
            if not helper(node.left, lower, val):
                return False
            if not helper(node.right, val, upper):
                return False
            return True
        
        return helper(root)

# test
if __name__ == "__main__":
    # 构建一个简单的二叉树
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    solution = Solution()
    print(solution.isValidBST(root))  # 输出: True

    # 构建一个不是二叉搜索树的例子
    root_invalid = TreeNode(5)
    root_invalid.left = TreeNode(1)
    root_invalid.right = TreeNode(4)
    root_invalid.right.left = TreeNode(3)
    root_invalid.right.right = TreeNode(6)

    print(solution.isValidBST(root_invalid))  # 输出: False
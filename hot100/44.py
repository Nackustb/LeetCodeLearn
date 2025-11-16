from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=0
        def dfs(node):
            nonlocal ans,k
            if node is None or k<0:
                return None
            left=dfs(node.left)
            k-=1
            if k==0:
                ans=node.val
            right=dfs(node.right)
        dfs(root)
        return ans
# test
if __name__ == "__main__":
    # 构建一个简单的二叉搜索树
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    k = 1
    solution = Solution()
    print(solution.kthSmallest(root, k))  # 输出: 1

    k = 2
    print(solution.kthSmallest(root, k))  # 输出: 2

    k = 3
    print(solution.kthSmallest(root, k))  # 输出: 3
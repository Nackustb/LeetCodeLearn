from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1  # 空路径和为0

        def dfs(node, currSum):
            if not node:
                return 0
            
            currSum += node.val
            # 检查有多少条路径满足 currSum - targetSum
            res = prefix[currSum - targetSum]
            
            # 更新前缀和
            prefix[currSum] += 1
            
            # 遍历左右子树
            res += dfs(node.left, currSum)
            res += dfs(node.right, currSum)
            
            # 回溯
            prefix[currSum] -= 1
            return res
        
        return dfs(root, 0)

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.dfs(root, 0, targetSum)
        
        
    def dfs(self, node, num, target):
        new_sum = num + node.val
        
        if not node.left and not node.right:
            return True if new_sum == target else False
        
        l = self.dfs(node.left, new_sum, target) if node.left else False
        r = self.dfs(node.right, new_sum, target) if node.right else False
        
        return l or r

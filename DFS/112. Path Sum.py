class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.dfs(root, 0, targetSum)
        
        
    def dfs(self, node, num, target):
        new_sum = num + node.val
        
        if not node.left and not node.right:
            if new_sum == target:
                return True
            else:
                return False
        
        if node.left:
            l = self.dfs(node.left, new_sum, target)
        else:
            l = False
            
        if node.right:
            r = self.dfs(node.right, new_sum, target)
        else:
            r = False
        
        return l or r

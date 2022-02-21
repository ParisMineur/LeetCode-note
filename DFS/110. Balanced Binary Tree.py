class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        self.res = True
        self.dfs(root)
        
        return self.res
    
    def dfs(self, node):
        if not node:
            return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        if abs(left - right) > 1:
            self.res = False
        
        return max(left, right) + 1

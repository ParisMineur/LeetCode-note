class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:      
        return self.dfs(root.left, root.right)
        
        
    def dfs(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        
        if left.val == right.val:
            a = self.dfs(left.left, right.right)
            b = self.dfs(left.right, right.left)
            return a and b
        else:
            return False

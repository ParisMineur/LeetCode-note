class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 
        return self.dfs(root)
        
    def dfs(self, node):
        if not node:
            return []
        return self.dfs(node.left) + [node.val] + self.dfs(node.right)
        
        
    ## second dfs() 
    '''
    def dfs(self, node):
        if not node:
            return     
        res = [node.val]
        
        left = self.dfs(node.left) if node.left else []
        right = self.dfs(node.right) if node.right else []
        
        return left + res + right
    '''

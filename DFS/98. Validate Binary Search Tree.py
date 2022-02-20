class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = self.dfs(root)
        return inorder == list(sorted(set(inorder)))
    
    def dfs(self, node):
        if not node:
            return []
        return self.dfs(node.left) + [node.val] + self.dfs(node.right)

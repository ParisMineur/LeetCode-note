class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []
        self.dfs(root, '')
        return self.res
    
    def dfs(self, node, path):
        if not node:
            return 
        path += str(node.val)
        if not node.left and not node.right:
            self.res.append(path)
        else:
            path += '->'
            self.dfs(node.left, path)
            self.dfs(node.right, path)

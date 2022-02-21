class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return 
        
        res = []
        self.dfs(root, targetSum, [], res)
        return res
        
    
    def dfs(self, node, sum, path, res):
        if not node:
            return
        
        if not node.left and not node.right and sum == node.val:
            path.append(node.val)
            res.append(path)
        else:
            self.dfs(node.left, sum-node.val, path+[node.val], res)
            self.dfs(node.right, sum-node.val, path+[node.val], res)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def inorder(root):  ## in-order traversal
            if root is None:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        inorder = inorder(root)
        return inorder == list(sorted(set(inorder)))

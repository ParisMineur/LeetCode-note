class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return None
        
        res = []
        
        d = collections.deque()  ## Doubly Ended Queue
        d.append(root)
        
        while d:
            l = len(d)
            level = []
            
            for _ in range(l):
                node = d.popleft()
                level.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
                
            res.append(level)
            
        return res

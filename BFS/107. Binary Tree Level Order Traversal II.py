class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        d = collections.deque()
        d.append(root)
        
        while d:
            l = len(d)
            temp = []
            
            for _ in range(l):
                node = d.popleft()
                if node:
                    temp.append(node.val)
                    
                    if node.left:
                        d.append(node.left)
                    if node.right:
                        d.append(node.right)
            res.append(temp)
            
        return res[::-1]

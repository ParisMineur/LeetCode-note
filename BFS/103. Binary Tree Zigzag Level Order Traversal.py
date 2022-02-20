class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        
        l2 = len(res)
        for i in range(l2):
            if i&1:
                res[i].reverse()
        
        return res

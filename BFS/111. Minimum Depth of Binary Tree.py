class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = 0
        
        d = collections.deque()
        d.append(root)
        
        b = False
        
        while d:
            
            l = len(d)
            
            for _ in range(l):
                node = d.popleft()
                if not node.left and not node.right:
                    b = True
                    break
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            res += 1
            
            if b == True:
                break
            
        return res

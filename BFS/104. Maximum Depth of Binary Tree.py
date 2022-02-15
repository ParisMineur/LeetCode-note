class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = 0
        
        d = collections.deque()
        d.append(root)
        
        while d:
            l = len(d)
            for _ in range(l):
                node = d.popleft()
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            res += 1
            
        return res

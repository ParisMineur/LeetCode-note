class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        d = collections.deque()
        d.append(root)
        res = []
        
        while d:
            l = len(d)
            temp = []
            
            for _ in range(l):
                node = d.popleft()
                temp.append(node)
                
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
                    
            res.append(temp)
            
        for a in res:
            l2 = len(a)
            for i in range(l2-1):
                a[i].next = a[i+1]
                
        return root

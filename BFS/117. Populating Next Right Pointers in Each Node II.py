class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        d = collections.deque()
        d.append(root)
        res = []
        
        while d:
            temp = []
            
            for _ in range(len(d)):
                node = d.popleft()
                temp.append(node)
                
                d.append(node.left) if node.left else 0
                d.append(node.right) if node.right else 0
                    
            res.append(temp)
            
        for a in res:
            for i in range(len(a)-1):
                a[i].next = a[i+1]
                
        return root

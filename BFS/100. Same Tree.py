class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        d1, d2 = collections.deque(), collections.deque()
        d1.append(p)
        d2.append(q)
        
        while d1 and d2:
            l1, l2 = len(d1), len(d2)
            if l1 != l2:
                return False
            
            for _ in range(l1):
                
                node1 = d1.popleft()
                node2 = d2.popleft()
                
                if not node1 and not node2:
                    continue
                elif (node1 or node2) and not (node1 and node2):
                    return False
                
                if node1.val != node2.val:
                    return False
                
                d1.append(node1.left)
                d1.append(node1.right)
                d2.append(node2.left)
                d2.append(node2.right)

        
        if not d1 and not d2:
            return True
        else:
            return False

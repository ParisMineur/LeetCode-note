class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        d1 = collections.deque()
        d2 = collections.deque()
        
        d1.append(root.left)
        d2.append(root.right)
        
        while d1 and d2:
            l1 = len(d1)
            l2 = len(d2)
            
            if l1 != l2:
                return False
            
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
            d2.append(node2.right)
            d2.append(node2.left)
            
        if not d1 and not d2:
            return True
        else:
            return False

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return
        
        d = collections.deque()
        d.append(root)
        
        while d:
            node = d.popleft()
            if node.left and node.right:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                d.append(node.left)
                d.append(node.right)

        return root

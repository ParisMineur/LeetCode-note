## template for BFS

def BFS(graph, start, end):
    queue = []
    queue.append(start)
    
    visited = set()  ## use set to store visited points
    visited.add(start)
    
    while queue:
        node = queue.pop()
        visited.add(node)
        
        process(node)  ## do something
        
        nodes = generate_related_nodes(node)  ## find related nodes which haven't been visited
        queue.append(nodes)

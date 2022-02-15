## template for DFS

visited = ser()
def DFS(node, visited):
    visited.add(node)
    
    precess(node)  ## do something
    
    for next_node in node.children():
        if not next_node in visited:
            DFS(next_node, visited)
         
    

from collections import deque
from typing import List, Any, Dict

class Tree:
    def __init__(self, graph: Dict[Any, List[Any]]) -> None:
        """
        Initializes a Tree object with the given graph.

        Parameters:
        - graph (Dict[Any, List[Any]]): An adjacency list representing the graph.
        """
        self.graph = graph
    
    def bfs(self, start: Any = None) -> List[Any]:
        """
        Performs Breadth-First Search (BFS) traversal on the graph.

        Parameters:
        - start (Any): The starting node for BFS. If not provided, uses the first node in the graph.

        Returns:
        - List[Any]: The BFS traversal order.
        """
        queue = deque()
        visited = set()
        
        # Start BFS algorithm
        start = start or list(self.graph.keys())[0]  # First element from the graph
        queue.append(start)
        traversal = []  # Corrected variable name
      
        while queue:
            node = queue.popleft()
            if node not in visited and node is not None:
                traversal.append(node)
                visited.add(node)
                children = self.graph[node]
                queue.extend(children)
        
        return traversal
    
    def dfs(self, start: Any = None) -> List[Any]:
        """
        Performs Depth-First Search (DFS) traversal on the graph.

        Parameters:
        - start (Any): The starting node for DFS. If not provided, uses the first node in the graph.

        Returns:
        - List[Any]: The DFS traversal order.
        """
        # Start DFS algorithm
        start = start or list(self.graph.keys())[0]  # First element from the graph
        visited = set()
        traversal = []  

        def dfs_helper(node):
            if node not in visited and node is not None:
                traversal.append(node)
                visited.add(node)
                for child_node in self.graph[node]:
                    dfs_helper(child_node)
        
        dfs_helper(start)
        return traversal


if __name__ == '__main__':

    # Example tree structure representation:
    #
    #        A
    #       / \
    #      B   C
    #     /|   |
    #    D E   F
    
    # Example graph as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C']
    }
    
    tree = Tree(graph)
    
    # BFS:
    bfs_traversal = tree.bfs() 
    print(*bfs_traversal)  # A B C D E F
    
    # DFS:
    dfs_traversal = tree.dfs() 
    print(*dfs_traversal)  # A B D E C F

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        """Adds a directed edge from node to neighbor."""
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def display(self):
        """Displays the adjacency list representation of the graph."""
        return self.graph

    def bfs(self, start):
        """Breadth-First Search (BFS) Traversal"""
        visited = set()
        queue = [start]
        result = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                result.append(node)
                queue.extend(self.graph.get(node, []))
        
        return result

    def dfs(self, start, visited=None):
        """Depth-First Search (DFS) Traversal"""
        if visited is None:
            visited = set()
        if start not in visited:
            visited.add(start)
            for neighbor in self.graph.get(start, []):
                self.dfs(neighbor, visited)
        return list(visited)

# Example Usage
graph = Graph()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "E")
graph.add_edge("D", "F")

print("Graph:", graph.display())  
print("BFS Traversal from A:", graph.bfs("A"))  # ['A', 'B', 'C', 'D', 'E', 'F']
print("DFS Traversal from A:", graph.dfs("A"))  # ['A', 'B', 'D', 'F', 'C', 'E']

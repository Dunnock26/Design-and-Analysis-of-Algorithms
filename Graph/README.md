
# Graph (Adjacency List)

## What is a Graph?

A graph in data structure is a non-linear data structure that represents relationships between objects using nodes and edges. Graphs are used to model and solve problems in many areas, including social networks, transportation, and the internet. 

## Real-Life Uses
* Social Networks

* Google Maps Navigation

* Web Crawlers

## Key Lines of Code
```
self.graph[node].append(neighbor)  # Adding an edge between two nodes
```
This maintains the adjacency list representation, ensuring efficient traversal and manipulation of connections.

## How to Run
Save the Python script and execute it using:
```
python graph.py
```

## Example Output
```
Graph: {'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'D': ['F']}
BFS Traversal from A: ['A', 'B', 'C', 'D', 'E', 'F']
DFS Traversal from A: ['A', 'B', 'D', 'F', 'C', 'E']
```

## Demo of the Program (Asciinema)
```
https://asciinema.org/a/iPJTW0dMNNU9S6c1lFiCSJeHN
```


# Heap (Min-Heap)

## What is a Heap?

A Heap is a special tree-based structure where the smallest (min-heap) or largest (max-heap) element is always at the top.

## Real-Life Uses
* Priority Queues (e.g., task scheduling, pathfinding algorithms like Dijkstra’s)

* Memory Management

* Sorting Algorithms (Heap Sort)

## Key Lines of Code
```
heapq.heappush(self.heap, item)  # Insert into heap while maintaining heap property
heapq.heappop(self.heap)         # Removes the smallest element, ensuring priority order
```
These operations ensure that the heap structure remains valid, allowing efficient retrieval of the smallest or largest element.

## How to Run
Save the Python script and execute it using:
```
python heap.py
```

## Example Output
```
Heap after insertions: [1, 3, 8, 5]
Peek: 1
Popped: 1
Heap after pop: [3, 5, 8]
```

## Demo of the Program (Asciinema)
```
https://asciinema.org/a/8de5krKpkcNIdU0WSnmgoYGPy
```
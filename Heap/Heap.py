import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        """Adds an item to the heap."""
        heapq.heappush(self.heap, item)

    def pop(self):
        """Removes and returns the smallest item."""
        if self.heap:
            return heapq.heappop(self.heap)
        return "Heap is empty"

    def peek(self):
        """Returns the smallest item without removing it."""
        if self.heap:
            return self.heap[0]
        return "Heap is empty"

    def display(self):
        """Displays the heap as a list."""
        return self.heap

# Example Usage
heap = MinHeap()
heap.push(5)
heap.push(3)
heap.push(8)
heap.push(1)

print("Heap after insertions:", heap.display())  # [1, 3, 8, 5] (Min-Heap)
print("Peek:", heap.peek())  # 1
print("Popped:", heap.pop())  # 1
print("Heap after pop:", heap.display())  # [3, 5, 8]

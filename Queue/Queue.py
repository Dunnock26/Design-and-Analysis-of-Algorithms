class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Adds an item to the queue (rear)."""
        self.queue.append(item)

    def dequeue(self):
        """Removes and returns the front item."""
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"

    def front(self):
        """Returns the front item without removing it."""
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"

    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Returns the number of elements in the queue."""
        return len(self.queue)

    def display(self):
        """Displays the queue (front to rear)."""
        return self.queue

# Example Usage
queue = Queue()
queue.enqueue("apple")
queue.enqueue("banana")
queue.enqueue("cherry")

print("Queue after enqueues:", queue.display())  # ['apple', 'banana', 'cherry']
print("Front:", queue.front())  # 'apple'
print("Dequeued:", queue.dequeue())  # 'apple'
print("Queue after dequeue:", queue.display())  # ['banana', 'cherry']
print("Is queue empty?", queue.is_empty())  # False

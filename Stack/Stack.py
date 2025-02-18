class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Adds an item to the top of the stack."""
        self.stack.append(item)

    def pop(self):
        """Removes and returns the top item of the stack."""
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        """Returns the top item without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        """Checks if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Returns the number of elements in the stack."""
        return len(self.stack)

    def display(self):
        """Displays the stack (top to bottom)."""
        return self.stack[::-1]  # Reverse for better visualization

# Example Usage
stack = Stack()
stack.push("apple")
stack.push("banana")
stack.push("cherry")

print("Stack after pushes:", stack.display())  # ['cherry', 'banana', 'apple']
print("Peek:", stack.peek())  # 'cherry'
print("Popped:", stack.pop())  # 'cherry'
print("Stack after pop:", stack.display())  # ['banana', 'apple']
print("Is stack empty?", stack.is_empty())  # False

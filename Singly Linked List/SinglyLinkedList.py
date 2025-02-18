class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Adds a new node at the end."""
        if not self.head:
            self.head = Node(data)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)

    def display(self):
        """Displays the linked list."""
        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result

# Example Usage
sll = SinglyLinkedList()
sll.append("apple")
sll.append("banana")
sll.append("cherry")

print("Singly Linked List:", sll.display())  # ['apple', 'banana', 'cherry']

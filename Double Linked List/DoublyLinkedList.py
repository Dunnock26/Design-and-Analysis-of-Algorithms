class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Adds a node at the end."""
        if not self.head:
            self.head = DNode(data)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        new_node = DNode(data)
        temp.next = new_node
        new_node.prev = temp

    def display(self):
        """Displays the linked list."""
        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result

# Example Usage
dll = DoublyLinkedList()
dll.append("apple")
dll.append("banana")
dll.append("cherry")

print("Doubly Linked List:", dll.display())  # ['apple', 'banana', 'cherry']

class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Adds a node to the end."""
        new_node = CNode(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        """Displays the circular linked list."""
        temp = self.head
        result = []
        if temp:
            while True:
                result.append(temp.data)
                temp = temp.next
                if temp == self.head:
                    break
        return result

# Example Usage
cll = CircularLinkedList()
cll.append("apple")
cll.append("banana")
cll.append("cherry")

print("Circular Linked List:", cll.display())  # ['apple', 'banana', 'cherry']

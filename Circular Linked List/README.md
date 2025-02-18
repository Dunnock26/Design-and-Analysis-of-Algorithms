
# Circular Linked List

## What is a Circular Linked List?

A Circular Linked List is a linked list where the last node points back to the first node.

## Real-Life Uses
* CPU Scheduling (Round-Robin Algorithm)

* Multiplayer Games (Turn-based systems)

* Continuous Music Playlists

## Key Lines of Code
```
new_node.next = self.head  # Last node points to head, forming a circular structure
```
This enables continuous traversal without reaching a None reference, ideal for cyclic operations.

## How to Run
Save the Python script and execute it using:
```
python circular_linked_list.py
```

## Example Output
```
Circular Linked List: ['apple', 'banana', 'cherry']
```

## Demo of the Program (Asciinema)
```
https://asciinema.org/a/iPJTW0dMNNU9S6c1lFiCSJeHN 
```
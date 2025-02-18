
# Doubly Linked List

## What is a Doubly Linked List?

A Doubly Linked List is a list where each node has a **next** and **prev** pointer.

## Real-Life Uses
* Browser Forward/Backward Navigation

* Music Playlists (Next/Previous Track)

* Undo/Redo operations

## Key Lines of Code
```
self.next = new_node  # Forward link to next node
self.prev = temp      # Backward link to previous node
```
This allows traversal in both directions, making it more flexible than a singly linked list.

## How to Run
Save the Python script and execute it using:
```
python doubly_linked_list.py
```

## Example Output
```
Doubly Linked List: ['apple', 'banana', 'cherry']
```

## Demo of the Program (Asciinema)
```
https://asciinema.org/a/fNksOvnLDds7fssN9l9mUD3dQ 
```
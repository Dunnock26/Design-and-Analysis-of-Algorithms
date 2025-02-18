
# Stack

## What is a Stack?

A stack is a data structure that follows the Last In, First Out (LIFO) principle, where elements are added and removed in a specific order.

## Real-Life Uses
* Memory Management (Recursion)

* Undo/Redo Operations

* Expression Evaluation

* Browser History

## Key Lines of Code
```
self.stack.append(item)  # Add elements to the top
return self.stack.pop()  # Removes recent item in stack
```
This structure allows efficient insertions and deletions without memory reallocation, unlike arrays.

## How to Run
Save the Python script and execute it using:
```
python stack.py
```

## Example Output
```
Stack after pushes: ['cherry', 'banana', 'apple']
Peek: cherry
Popped: cherry
Stack after pop: ['banana', 'apple']
Is stack empty? False
```

## Demo of the Program (Asciinema)
```
https://asciinema.org/a/qXFTycby5wbov2giARv8SIoXe
```
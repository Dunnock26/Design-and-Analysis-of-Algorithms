
# Queue

## What is a Queue?

A Queue is a linear data structure that follows the FIFO (First In, First Out) principle. The first element added is the first one to be removed.

## Real-Life Uses
Print Queue in a Printer

Customer Service Call Queue

Task Scheduling in OS

## Key Lines of Code
```
self.queue.append(item)  # Enqueue

self.queue.pop(0)        # Dequeue
```
## How to Run
Sve the Python script and execute it using:
```
python queue.py
```

## Example Output
```
Queue after enqueues: ['apple', 'banana', 'cherry']
Front: apple
Dequeued: apple
Queue after dequeue: ['banana', 'cherry']
Is queue empty? False
```
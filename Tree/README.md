
# Tree (Binary Search Tree)

## What is a Tree?

A Tree is a hierarchical data structure where each node has a parent and may have multiple children. A Binary Search Tree (BST) is a tree where each node follows the property: left child < parent < right child.

## Real-Life Uses
* File System Organization

* Database Indexing (e.g., B-Trees in SQL Databases)

* AI Decision Trees (e.g., Minimax Algorithm in Games)

## Key Lines of Code
```
if value < node.value:
    node.left = insert(node.left, value)  # Inserts into the left subtree if smaller
else:
    node.right = insert(node.right, value)  # Inserts into the right subtree if larger
```
This ensures that the tree maintains its sorted structure, enabling efficient searching, insertion, and deletion.

## How to Run
Save the Python script and execute it using:
```
python tree.py
```

## Example Output
```
Inorder Traversal: ['apple', 'banana', 'cherry', 'date', 'elderberry']
```
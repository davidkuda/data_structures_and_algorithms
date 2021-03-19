# Nodes

### The Concept of a Node

A node is a fundamental building block of many data structures. A node consist of two elements: Data and links to other nodes. The data may be a variety of types, e.g. an integer, a floating point, a string, a list, a dictionary; You name it.

The link (or the links) are also referred to as "pointers" since a node "points" to other nodes. An empty link (None / null) signals the end of the current path. 

If you remove the pointer of a node, a series of linked nodes may be "lost". This is referred to as an "orphaned node". So to delete a node or a link to a node it's important to not just set it to None but to connect the previous node to the next node. 

### Nodes implemented in Python

In this example I create the class `Node` with the two attributes `value` and `link_node`. The former is required, a node has to be instantiated with a value. The latter, however, may be None, since a link to another node is not required but would signal that the end of a path (e.g. "linked list" or "queue") is reached.

```python
class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link = link
```

To retrieve either the value or the link I will implement the respective getter method, `get_value` and `get_link`.

```python
  def get_value(self):
    return self.value

  def get_link_node(self):
    return self.link
```

To set the link I will implement a set method, `set_link`. This method takes a `node` as an argument. 

```python
  def set_link_node(self, link):
    self.link = link
```
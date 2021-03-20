# Linked Lists

### The Concept of a Linked List

A linked list is a series of nodes that are connected together. A node has data and a link to another node. The __head node__ refers to the first node of the Linked List. The data structure of a linked lists is a foundation for more complex data structures. Since the nodes use links to denote the next node in the sequence, the nodes are not required to be sequentially located in memory. The links can either be unidirectional by only pointing to the next node or bidirectional by point to the previous node, too. 

![A diagram of a linked list](img/linked_list.png)

Common operations on a linked list may include:

- adding nodes
- removing nodes
- finding a node
- traversing the linked list

__Adding a new node__ to the beginning of the list requires you to link your new node to the current head node. This way, you maintain your connection with the following nodes in the list.

__Removing a node__ requires you to adjust the pointers. The previous node should point to the next node. That way, the middle node gets "orphaned" and essentially deleted. 


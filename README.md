# Data Structures

## Node: An individual part of a larger data structure
Nodes are a basic data structure which contain data and one or more links to other nodes. Nodes can be used to represent a tree structure or a linked list. In such structures where nodes are used, it is possible to traverse from one node to another node.

![many nodes](https://content.codecademy.com/practice/art-for-practice/many-nodes.png)

### Orphaned nodes
Nodes that have no links pointing to them except for the head node, are considered “orphaned.” In the illustration, if the nodes a2 and a5 are removed, they will be orphaned.

![orphaned nodes](https://content.codecademy.com/practice/art-for-practice/orphaned_nodes.png)

### Null node link
Data structures containing nodes have typically two bits of information stored in a node: data and link to next node.

The first part is a value and the second part is an address of sorts pointing to the next node. In this way, a system of nodes is created. A NULL value in the link part of a node’s info denotes that the path or data structure contains no further nodes.

### Removing a node from the middle of a linked list
When removing a node from the middle of a linked list, it is necessary to adjust the link on the previous node so that it points to the following node. In the given illustration, the node a1 must point to the node a3 if the node a2 is removed from the linked list.

![](https://content.codecademy.com/practice/art-for-practice/removing_a_node.png)

## LinkedList (Singly-Linked)
A linked list is a linear data structure where elements are not stored at contiguous location. Instead the elements are linked using pointers.

In a linked list data is stored in nodes and each node is linked to the next and, optionally, to the previous. Each node in a list consists of the following parts:

1. data 
1. A pointer (Or reference) to the next node 
1. Optionally, a pointer to the previous node

![linked list](https://www.geeksforgeeks.org/wp-content/uploads/gq/2013/03/Linkedlist.png)

### Adding a new head node in a linked list
When adding a new node to the start of a linked list, it is necessary to maintain the list by giving the new head node a link to the current head node. For instance, to add a new node a0 to the begining of the linked list, a0 should point to a1.
![](https://content.codecademy.com/practice/art-for-practice/new_head_node.png)
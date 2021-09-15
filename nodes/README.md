
___
## Node: An individual part of a larger data structure
___
Nodes are a basic data structure which contain data and one or more links to other nodes. Nodes can be used to represent a tree structure or a linked list. In such structures where nodes are used, it is possible to traverse from one node to another node.

<details open><summary><em><b>Many Nodes</b></em></summary>
<br>

![many nodes](https://content.codecademy.com/practice/art-for-practice/many-nodes.png)

</details>
<br>

### Orphaned nodes
Nodes that have no links pointing to them except for the head node, are considered “orphaned.” In the illustration, if the nodes `a2` and `a5` are removed, they will be orphaned.


<details open><summary><em><b>Orphaned Nodes</b></em></summary>
<br>

![orphaned nodes](https://content.codecademy.com/practice/art-for-practice/orphaned_nodes.png)

</details>
<br>


### Null node link
Data structures containing nodes have typically two bits of information stored in a node: data and link to next node.

The first part is a value and the second part is an address of sorts pointing to the next node. In this way, a system of nodes is created. A `NULL` value in the link part of a node’s info denotes that the path or data structure contains no further nodes.

### Removing a node from the middle of a linked list
When removing a node from the middle of a linked list, it is necessary to adjust the link on the previous node so that it points to the following node. In the given illustration, the node `a1` must point to the node `a3` if the node `a2` is removed from the linked list.

<details open><summary><em><b>Removing a Node</b></em></summary>
<br>

![removing a node](https://content.codecademy.com/practice/art-for-practice/removing_a_node.png)


</details>
<br>

### Python Node implementation
A Node is a data structure that stores a value that can be of any data type and has a pointer to another node. The implementation of a Node class in a programming language such as Python, should have methods to get the value that is stored in the Node, to get the next node, and to set a link to the next node.

<details open><summary><em><b>Node Class</b></em></summary>
<br>

```python
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node
  
  def get_value(self):
    return self.value
 
```

</details>
<br>

### Python DoublyLinkedList Node Implementation

__Doubly linked lists__ in Python utilize an updated Node class that has a pointer to the previous node. This comes with additional setter and getter methods for accessing and updating the previous node.

<details open ><summary><em><b>Updated Node Class</b></em></summary>
<br>

```python
class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node
 
  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value
```

</details>
<br>


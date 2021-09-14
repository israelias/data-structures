# Data Structures

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


<details><summary><em><b>Orphaned Nodes</b></em></summary>
<br>

![orphaned nodes](https://content.codecademy.com/practice/art-for-practice/orphaned_nodes.png)

</details>
<br>


### Null node link
Data structures containing nodes have typically two bits of information stored in a node: data and link to next node.

The first part is a value and the second part is an address of sorts pointing to the next node. In this way, a system of nodes is created. A `NULL` value in the link part of a node’s info denotes that the path or data structure contains no further nodes.

### Removing a node from the middle of a linked list
When removing a node from the middle of a linked list, it is necessary to adjust the link on the previous node so that it points to the following node. In the given illustration, the node `a1` must point to the node `a3` if the node `a2` is removed from the linked list.

<details><summary><em><b>Removing a Node</b></em></summary>
<br>

![removing a node](https://content.codecademy.com/practice/art-for-practice/removing_a_node.png)


</details>
<br>

### Python Node implementation
A Node is a data structure that stores a value that can be of any data type and has a pointer to another node. The implementation of a Node class in a programming language such as Python, should have methods to get the value that is stored in the Node, to get the next node, and to set a link to the next node.

<details ><summary><em><b>Node Class</b></em></summary>
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

___
## LinkedList (Singly-Linked)
___
A __linked list__ is a linear data structure where elements are not stored at contiguous location. Instead the elements are linked using pointers.

In a linked list data is stored in nodes and each node is linked to the next and, optionally, to the previous. Each node in a list consists of the following parts:

1. data 
1. A pointer (Or reference) to the next node 
1. Optionally, a pointer to the previous node

<details open><summary><em><b>Linked List</b></em></summary>
<br>

![linked list](https://www.geeksforgeeks.org/wp-content/uploads/gq/2013/03/Linkedlist.png)


</details>
<br>


### Adding a new head node in a linked list
When adding a new node to the start of a linked list, it is necessary to maintain the list by giving the new head node a link to the current head node. For instance, to add a new node `a0` to the begining of the linked list, `a0` should point to `a1`.

<details ><summary><em><b>New Head Node</b></em></summary>
<br>

![new head node](https://content.codecademy.com/practice/art-for-practice/new_head_node.png)


</details>
<br>

### The Head Node in Linked Lists
The first node in a linked list is called the head node. If the linked list is empty, then the value of the head node is `NULL`.

<details open><summary><em><b>Linked List Head Node</b></em></summary>
<br>

![linked list head node](https://cdn-images-1.medium.com/max/2560/1*GOKmkucFHN_gmTMUtyC2sQ.png)


</details>
<br>

### Implementing a linked list
A linked list exposes the ability to traverse the list from one node to another node. The starting node is considered the head node from where the list can be traversed.

<details ><summary><em><b>Linked List Implementation</b></em></summary>
<br>

![linked list implementation](https://content.codecademy.com/practice/art-for-practice/linked-list.png)


</details>
<br>

### Linked List Data Structure
A linked list is a data structure that consists of a list of nodes. Each node contains data and a link to the next node. As shown below, you can implement a LinkedList class in Python, utilizing a Python implementation of the Node class.



<details ><summary><em><b>Linked List Class</b></em></summary>
<br>

```python
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
 
  def get_head_node(self):
    return self.head_node
 
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
 
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
 
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node
```

</details>
<br>

___
## LinkedList (Doubly-Linked)
___
__Doubly linked lists__ in Python utilize an updated Node class that has a pointer to the previous node. This comes with additional setter and getter methods for accessing and updating the previous node.

<details ><summary><em><b>Updated Node Class</b></em></summary>
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

### Constructor
A Python __DoublyLinkedList__ class constructor should store:

- A `head_node` property to store the head of the list
- A `tail_node` property to store the tail of the list

The `head_node` and `tail_node` are set to None as their defaults.

<details ><summary><em><b>DoublyLinkedList Class Constructor</b></em></summary>
<br>

```python
class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None
```

</details>
<br>


### Adding to the Tail

A Python __DoublyLinkedList__ class can implement an `.add_to_tail()` instance method for adding new data to the tail of the list. `.add_to_tail()` takes a single `new_value` argument. It uses `new_value` to create a new `Node` which it adds to the tail of the list.

<details ><summary><em><b>Add to tail</b></em></summary>
<br>

```python
 def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node
 
    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)
 
    self.tail_node = new_tail
 
    if self.head_node == None:
      self.head_node = new_tail
```

</details>
<br>

### Adding to the Head

A Python __DoublyLinkedList__ class can implement an `.add_to_head()` instance method for adding new data to the head of the list. `.add_to_head()` takes a single new_value argument. It uses `new_value` to create a new `Node` which it adds to the head of the list.

<details ><summary><em><b>Add to head</b></em></summary>
<br>

```python
def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node
 
    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)
 
    self.head_node = new_head
 
    if self.tail_node == None:
      self.tail_node = new_head
```

</details>
<br>


### Removing the Tail
A Python __DoublyLinkedList__ class can implement a `.remove_tail()` instance method for removing the head of the list. `.remove_tail()` takes no arguments. It removes and returns the tail of the list, and sets the tail’s previous node as the new tail.

<details ><summary><em><b>Remove tail</b></em></summary>
<br>

```python
def remove_tail(self):
    removed_tail = self.tail_node
 
    if removed_tail == None:
      return None
 
    self.tail_node = removed_tail.get_prev_node()
 
    if self.tail_node != None:
      self.tail_node.set_next_node(None)
 
    if removed_tail == self.head_node:
      self.remove_head()
 
    return removed_tail.get_value()
```

</details>
<br>

### Removing by Value
A Python __DoublyLinkedList__ class can implement a `.remove_by_value()` instance method that takes `value_to_remove` as an argument and returns the node that matches `value_to_remove`, or `None` if no match exists. If the node exists, `.remove_by_value()` removes it from the list and correctly resets the pointers of its surrounding nodes.

<details ><summary><em><b>Remove by value</b></em></summary>
<br>

```python
def remove_by_value(self, value_to_remove):
    node_to_remove = None
    current_node = self.head_node
 
    while current_node != None:
      if current_node.get_value() == value_to_remove:
        node_to_remove = current_node
        break
 
      current_node = current_node.get_next_node()
 
    if node_to_remove == None:
      return None
 
    if node_to_remove == self.head_node:
      self.remove_head()
    elif node_to_remove == self.tail_node:
      self.remove_tail()
    else:
      next_node = node_to_remove.get_next_node()
      prev_node = node_to_remove.get_prev_node()
      next_node.set_prev_node(prev_node)
      prev_node.set_next_node(next_node)
 
    return node_to_remove
```

</details>
<br>

### Removing the Head
A Python __DoublyLinkedList__ class can implement a `.remove_head()` instance method for removing the head of the list. `.remove_head()` takes no arguments. It removes and returns the head of the list, and sets the head’s next node as the new head.

<details ><summary><em><b>Remove head</b></em></summary>
<br>

```python
def remove_head(self):
    removed_head = self.head_node
 
    if removed_head == None:
      return None
 
    self.head_node = removed_head.get_next_node()
 
    if self.head_node != None:
      self.head_node.set_prev_node(None)
 
    if removed_head == self.tail_node:
      self.remove_tail()
 
    return removed_head.get_value()
```

</details>
<br>

### DoublyLinkedList Data Structure Overview

A __DoublyLinkedList__ class in Python has the following functionality:

- A constructor with head_node and tail_node properties
- An `.add_to_head() `method to add new nodes to the head
- An `.add_to_tail()` method to add new nodes to the tail
- A `.remove_head()` method to remove the head node
- A `.remove_tail() `method to remove the tail node
- A `.remove_by_value()` method to remove a node that matches the value_to_remove passed in

<details ><summary><em><b>DoublyLinkedList Class</b></em></summary>
<br>

```python
class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None
 
  
  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node
 
    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)
 
    self.head_node = new_head
 
    if self.tail_node == None:
      self.tail_node = new_head
 
 
  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node
 
    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)
 
    self.tail_node = new_tail
 
    if self.head_node == None:
      self.head_node = new_tail
 
 
  def remove_head(self):
    removed_head = self.head_node
 
    if removed_head == None:
      return None
 
    self.head_node = removed_head.get_next_node()
 
    if self.head_node != None:
      self.head_node.set_prev_node(None)
 
    if removed_head == self.tail_node:
      self.remove_tail()
 
    return removed_head.get_value()
 
 
  def remove_tail(self):
    removed_tail = self.tail_node
 
    if removed_tail == None:
      return None
 
    self.tail_node = removed_tail.get_prev_node()
 
    if self.tail_node != None:
      self.tail_node.set_next_node(None)
 
    if removed_tail == self.head_node:
      self.remove_head()
 
    return removed_tail.get_value()
 
 
  def remove_by_value(self, value_to_remove):
    node_to_remove = None
    current_node = self.head_node
 
    while current_node != None:
      if current_node.get_value() == value_to_remove:
        node_to_remove = current_node
        break
 
      current_node = current_node.get_next_node()
 
    if node_to_remove == None:
      return None
 
    if node_to_remove == self.head_node:
      self.remove_head()
    elif node_to_remove == self.tail_node:
      self.remove_tail()
    else:
      next_node = node_to_remove.get_next_node()
      prev_node = node_to_remove.get_prev_node()
      next_node.set_prev_node(prev_node)
      prev_node.set_next_node(next_node)
 
    return node_to_remove
```

</details>
<br>


___
## Queues
___

### Queues data structure methods
The queue data structure has three main methods:

- `enqueue` (adds a node to the back of the queue)
- `dequeue` (removes node at the front of the queue)
- `peek` (returns value of node at the front of the queue, without removing it)

### Queue follows FIFO protocol
A queue is a data structure composed of nodes, which follows a first in, first out (FIFO) protocol.

This is analogous to a line at a grocery store, for which the first customer in the queue is the first to checkout.

___
## Stacks
___
A _stack_ is a data structure that follows a last in, first out (LIFO) protocol. The latest node added to a stack is the node which is eligible to be removed first. If three nodes (`a`, `b` and, `c`) are added to a stack in this exact same order, the node `c` must be removed first. The only way to remove or return the value of the node `a` is by removing the nodes `c` and `b`.

<details open ><summary><em><b>Stack</b></em></summary>
<br>

![stack](https://content.codecademy.com/practice/art-for-practice/stack.png)


</details>
<br>

### Stack _overflow_
Every stack has a size that determines how many nodes it can accommodate. Attempting to push a node in a full stack will result in a stack overflow. The program may crash due to a stack overflow.

A stack is illustrated in the given image. `stackA.push(xg)` will result in a stack overflow since the stack is already full.

### Main methods of a stack data structure

The stack data structure has three main methods: 

- `push()` adds a node to the top of the stack.
- `pop()`  removes a node from the top of the stack
- `peek()`  returns the value of the top node without removing it from the stack

### Stack data structure
A Stack is a data structure that supports two basic operations: pushing a new item to the top of the stack and popping a single item from the top of the stack.

In order to implement a stack using a node class, we have to store a node that is currently referencing the top of the stack and update it during the push and pop operations.

<details ><summary><em><b>Stack Class</b></em></summary>
<br>

```python
from node import Node
 
class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
    else:
      print("All out of space!")
 
  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This stack is totally empty.")
  
  def peek(self):
    if self.size > 0:
      return self.top_item.get_value()
    else:
      print("Nothing to see here!")
  
  def has_space(self):
    return self.limit > self.size
  
  def is_empty(self):
    return self.size == 0
```

</details>
<br>

___
## Hash Maps
___
Hash maps are a common data structure used to store key-value pairs for efficient retrieval. A value stored in a hash map is retrieved using the key under which it was stored.

<details ><summary><em><b>hash map simplified</b></em></summary>
<br>

```python

# `states` is a Hash Map with state abbreviation keys and state name values.
 
states = {
  'TN': "Tennessee",
  'CA': "California",
  'NY': "New York",
  'FL': "Florida"
}
 
west_coast_state = states['CA']
```

</details>
<br>


### Hash function
Hash map data structures use a hash function, which turns a key into an index within an underlying array. The hash function can be used to access an index when inserting a value or retrieving a value from a hash map.

### Hash map underlying data structure
Hash maps are built on top of an underlying array data structure using an indexing system.

Each index in the array can store one key-value pair. If the hash map is implemented using chaining for collision resolution, each index can store another data structure such as a linked list, which stores all values for multiple keys that hash to the same index.

### hash map only one value
Each Hash Map key can be paired with only one value. However, different keys can be paired with the same value.

<details ><summary><em><b>hash map one value with many keys</b></em></summary>
<br>

```python

#This is a valid Hash Map where 2 keys share the same value
correct_hash_map = {
  "a" : 1,
  "b" : 3,
  "c" : 1
}
 
#This Hash Map is INVALID since a key cannot have more than 1 value
incorrect_hash_map = {
  "a" : 1,
  "a" : 3,
  "b" : 2
}
```

</details>
<br>

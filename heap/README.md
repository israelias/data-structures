## Heaps

### Heap Implementation
Heaps are typically implemented with a data structure such as an array or Python list. These sequential structures allow access to elements in a particular order which is key to efficient use of heaps. Although binary trees are helpful for understanding the relationships between nodes of a heap, implementation using a tree is less efficient for storage and retrieval of elements.

<details open ><summary><em><b>Heaps</b></em></summary>
<br>

![heaps](https://content.codecademy.com/practice/art-for-practice/new-pngs/heaps-representation.png)


</details>
<br>

### Adding Elements: Heapify Up
When a new element is added to a heap, if heap properties are violated, the new child must swap with its parent until both child and root properties are restored. This process is called _heapifying up_, because of the upwards movement of the new element in this restorative process.

<details open ><summary><em><b>Heapify Up</b></em></summary>
<br>

![heap up](https://content.codecademy.com/programs/cs-path/heaps-conceptual/heapup.gif)


</details>
<br>

### Heaps as Binary Trees
A proper representation of a heap is a _complete binary tree_, which is a [tree](#trees) whose nodes have at most two children, and whose levels are filled completely from left to right (with no gaps in children). It’s possible for the last level to be semi-completely filled, but all of its nodes are as far left as possible.

<details open ><summary><em><b>Heaps - Binary Tree</b></em></summary>
<br>

![heaps as Binary Tree](https://content.codecademy.com/practice/art-for-practice/new-pngs/heaps-intro.png)


</details>
<br>

### The Heap Class
The basis of a Heap class in Python is the implementation of a heap with a list, based on the parent-child relationships that a binary tree structure portrays. The class also consists of multiple methods that provide the functionality to construct these parent-child relationships in the list, add elements, remove the root element, and heapify in both directions when necessary.

<details open><summary><em><b>Heap Class</b></em></summary>
<br>

```python
class MinHeap:
  "Some key methods to be included in the MinHeap class"
  
  def __init__(self):
    "Creates a list and count variable"
    self.heap_list = [None]
    self.count = 0
    
  def retrieve_min(self):
    "Replaces root with last child, calls .heapify-down()"
    
  def add(self, element):
    "Adds new element to heap_list, calls heapify_up()"
    
  def get_smaller_child_idx(self, idx):
    "Returns the child a parent should swap with"
    
  def heapify_up(self): 
    "Implements heapify up"
    
  def heapify_down(self):
    "Implements heapify down"
```

</details>
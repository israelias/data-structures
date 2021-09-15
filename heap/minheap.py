class MinHeap:
    # MinHeap tracks the minimum element as the element at 
    # index 1 within an internal Python list.
    # When adding elements, we use .heapify_up() to compare the 
    # new element with its parent, making swaps if it violates the
    # heap property: children must be greater than their parents.
    # When removing the minimum element, we swap it with the last 
    # element in the list. Then we use .heapify_down() to compare
    # the new root with its children, swapping with the smaller 
    # child if necessary.
    def __init__(self):
        # Creates a list and count variable
        self.heap_list = [None]
        self.count = 0

    # HEAP HELPER METHODS
    # DO NOT CHANGE!
    # “child” and “parent” elements are determined by their relative indices 
    # within the internal list. By doing some arithmetic on an element’s index, 
    # we can determine the indices for parent and child elements (if they exist).
    def parent_idx(self, idx):
        # heap.parent_idx(4)
        # (4 // 2) == 2
        # Element at index 4 is 61 
        # Element at index 2 is 13
        # The parent element of 61 is 13
        return idx // 2

    def left_child_idx(self, idx):
        # heap.left_child(3)
        # (3 * 2) == 6
        # Element at index 3 is 21
        # Element at index 6 is 23
        # The left child element of 21 is 23
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count

    # END OF HEAP HELPER METHODS
    
    # Some key methods to be included in the MinHeap class
    
    # Replaces root with last child, calls .heapify-down()
    def retrieve_min(self):
        if self.count == 0:
            print("No items in heap")
            return None
    
        min = self.heap_list[1]
        print("Removing: {0} from {1}".format(min, self.heap_list))
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1 # swap
        self.heap_list.pop() # swap
        print("Last element moved to first: {0}".format(self.heap_list))    
        self.heapify_down()
        return min
            
    
    # Adds new element to heap_list, calls heapify_up()   
    def add(self, element):
        self.count += 1
        print("Adding: {0} to {1}".format(element, self.heap_list))
        self.heap_list.append(element)
        self.heapify_up()
        
    
     # Returns the child a parent should swap with
    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            print("There is only a left child")
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child < right_child:
                print("Left child is smaller")
                return self.left_child_idx(idx)
            else:
                print("Right child is smaller")
                return self.right_child_idx(idx)
       
    
    # Implements heapify up
    def heapify_up(self): 
        idx = self.count
        while self.parent_idx(idx) > 0:
            if self.heap_list[self.parent_idx(idx)] > self.heap_list[idx]:
                tmp = self.heap_list[self.parent_idx(idx)]
                print("swapping {0} with {1}".format(tmp, self.heap_list[idx]))
                self.heap_list[self.parent_idx(idx)] = self.heap_list[idx]
                self.heap_list[idx] = tmp
                
            idx = self.parent_idx(idx)
        
        print("HEAP RESTORED! {0}".format(self.heap_list))
        print("")

    # def heapify_up(self):
    #     print("Heapifying up")
    #     idx = self.count
    #     while self.parent_idx(idx) > 0:
    #         child = self.heap_list[idx]
    #         parent = self.heap_list[self.parent_idx(idx)]
    #         if parent > child:
    #             print("swapping {0} with {1}".format(parent, child))
    #             self.heap_list[idx] = parent
    #             self.heap_list[self.parent_idx(idx)] = child
    #         idx = self.parent_idx(idx)
    #     print("Heap Restored {0}".format(self.heap_list))
        
    # Implements heapify down
    def heapify_down(self):
        idx = 1
        while self.child_present(idx):
            smaller_child_idx = self.get_smaller_child_idx(idx)
            if self.heap_list[idx] > self.heap_list[smaller_child_idx]:
                tmp = self.heap_list[smaller_child_idx]
                print("swapping {0} with {1}".format(self.heap_list[idx], tmp))
                self.heap_list[smaller_child_idx] = self.heap_list[idx]
                self.heap_list[idx] = tmp

            idx = smaller_child_idx
        print("HEAP RESTORED! {0}".format(self.heap_list))
        print("")    

       
       
       
      # count swaps 
# class MinHeap:
#       def __init__(self):
#     self.heap_list = [None]
#     self.count = 0

#   def parent_idx(self, idx):
#     return idx // 2

#   def left_child_idx(self, idx):
#     return idx * 2

#   def right_child_idx(self, idx):
#     return idx * 2 + 1

#   def child_present(self, idx):
#     return self.left_child_idx(idx) <= self.count
  
#   def retrieve_min(self):
#     if self.count == 0:
#       print("No items in heap")
#       return None
    
#     min = self.heap_list[1]
#     self.heap_list[1] = self.heap_list[self.count]
#     self.count -= 1
#     self.heap_list.pop()
#     self.heapify_down()
#     return min

#   def add(self, element):
#     self.count += 1
#     self.heap_list.append(element)
#     self.heapify_up()


#   def get_smaller_child_idx(self, idx):
#     if self.right_child_idx(idx) > self.count:
#       return self.left_child_idx(idx)
#     else:
#       left_child = self.heap_list[self.left_child_idx(idx)]
#       right_child = self.heap_list[self.right_child_idx(idx)]
#       if left_child < right_child:
#         return self.left_child_idx(idx)
#       else:
#         return self.right_child_idx(idx)
    
#   def heapify_up(self):
#     idx = self.count
#     swap_count = 0
#     while self.parent_idx(idx) > 0:
#       if self.heap_list[self.parent_idx(idx)] > self.heap_list[idx]:
#         swap_count += 1
#         tmp = self.heap_list[self.parent_idx(idx)]
#         self.heap_list[self.parent_idx(idx)] = self.heap_list[idx]
#         self.heap_list[idx] = tmp
#       idx = self.parent_idx(idx)

#     element_count = len(self.heap_list)
#     if element_count > 10000:
#       print("Heap of {0} elements restored with {1} swaps"
#             .format(element_count, swap_count))
#       print("")    
      
#   def heapify_down(self):
#     idx = 1
#     # starts at 1 because we swapped first and last elements
#     swap_count = 1
#     while self.child_present(idx):
#       smaller_child_idx = self.get_smaller_child_idx(idx)
#       if self.heap_list[idx] > self.heap_list[smaller_child_idx]:
#         swap_count += 1
#         tmp = self.heap_list[smaller_child_idx]
#         self.heap_list[smaller_child_idx] = self.heap_list[idx]
#         self.heap_list[idx] = tmp
#       idx = smaller_child_idx

#     element_count = len(self.heap_list)
#     if element_count >= 10000:
#       print("Heap of {0} elements restored with {1} swaps"
#             .format(element_count, swap_count))
#       print("")  

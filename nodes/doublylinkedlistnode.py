from .basenode import Node as BaseNode

# Inherit from Base
# Add prev_node to constructor
# Methods set_next_node, get_next_node, get_value should be accessible

class Node(BaseNode):
    def __init__(self, value, next_node=None, prev_node=None):
        super(Node, self).__init__(value, next_node)
        self.prev_node = prev_node
        
    # def set_next_node(self, next_node):
    #     self.next_node = next_node
    
    # def get_next_node(self):
    #     return self.next_node
 
    def set_prev_node(self, prev_node):
        self.prev_node = prev_node
    
    def get_prev_node(self):
        return self.prev_node
  
    # def get_value(self):
    #     return self.value
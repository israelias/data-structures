from linked_list import Node, LinkedList
from blossom_lib import flower_definitions 

# The underlying data structure for Blossom is going to be a key-value store 
# that uses the common names for flowers as the key and saves the floral meaning
# of the flower as the value.

# In order to implement this functionality, this hash map is built with separate
# chains of linked lists at every index.

class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [LinkedList() for item in range(self.array_size)]

  # the __internal methods__ needed to perform the basic 
  # responsibilities of a hash map: .hash() and .compress().
  
  # .hash()
  def hash(self, key):
    # calculate the number for the string key by summing up the character encodings
    # of each character in the string
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    print('Encoding {0} into {1} with a hash value of {2}'.format(key, key_bytes, hash_code))
    return hash_code

  
  # .compress
  def compress(self, hash_code):
    # function that reduces the hash_code number into an array index.
    # takes has_code,returns the result of calculating the remainder of 
    # dividing hash_code by the length of the array (self.array.size)
    print('Compressing hash code {0} based on the size {1} to {2}'.format(hash_code, self.array_size, hash_code % self.array_size))
    return hash_code % self.array_size

  # the __external methods__ for interacting with 
  # the hash map: .assign() and .retrieve()
  
  # .assign()
  def assign(self, key, value):
    # method that gets the hash code by plugging `key` into .hash(),
    # and then gets the array index by plugging the resulting hash code into `.compress()`
    
    print('Assigning key: {0}, value:{1}...'.format(key, value))
    
    # the index address computed by `.compress()`
    array_index = self.compress(self.hash(key))
    
    # construct a Node object with the value of an array with key at 0 and value at 1 `[key, value]`
    # to be inserted at `list_at_array` if the key exists there
    payload = Node([key, value])
    
    # the LinkedList object instantiated at this location (computed `array_index`) in `self.array`
    list_at_array = self.array[array_index]
    
    print('Assignment attempt: Checking if key {0} already exists at {1}...'.format(key, list_at_array))

    for item in list_at_array:
      if item[0] == key:
        print('...Assignment key {0} found'.format(key))
        print('...Assigning {0} and overwriting the previous value of {1} at this location.'.format(key, item[1]))
        item[1] = value

    print('Assignment Check Result: No Existing Nodes with the same key')
    print('Assignment is clash-free')
    print('Assignment wrap up: Creating Node {0} and inserting into {1}'.format(payload, list_at_array))
    list_at_array.insert(payload)

  # `.retrieve()`
  def retrieve(self, key):
    # method that finds the hash code for `key` by plugging it into `.hash()`,
    # and then finds the array index by plugging that hash code into `.compress()`
    
    print('Retrieving {0}...'.format(key))
    
    # the index address computed by `.compress()` i.e. `7`
    array_index = self.compress(self.hash(key))
    
    # the LinkedList object instantiated at this location (computed `array_index`) in `self.array`
    list_at_index = self.array[array_index]
    
    print('Retrieval attempt: Checking if {0} is at {1}'.format(key, list_at_index))

    for item in list_at_index:
      if item[0] == key:
        print('...Retrieval Success of key {0} with value {1}'.format(key, item[1]))
        print('Retrievel wrap up: Successfully retrieved {0}'.format( key))
        return item[1]
      else:
        print('!...Retrievel Error: Found key {0} instead of {1}'.format(item[0], key))
        print('Retrievel wrap up: Failed to retrieve {0} due to clash.'.format( key))
        return None
    
blossom = HashMap(len(flower_definitions))

for flower in flower_definitions:
  print(' ')
  blossom.assign(flower[0], flower[1])
  print(' ')

blossom.retrieve('daisy')
print(' ')
blossom.retrieve('sunflower')
print(' ')
blossom.retrieve('magnolia')
print(' ')
blossom.retrieve('rose')
print(' ')
blossom.retrieve('wisteria')
print(' ')
blossom.retrieve('carnation')

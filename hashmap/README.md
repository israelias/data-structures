___
## Hash Maps
___
Hash maps are a common data structure used to store key-value pairs for efficient retrieval. A value stored in a hash map is retrieved using the key under which it was stored.

<details open><summary><em><b>hash map simplified</b></em></summary>
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

<details open><summary><em><b>hash map one value with many keys</b></em></summary>
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

### Creating the Hash Map Class
Hash maps are efficient key-value stores. They are capable of assigning and retrieving data in the fastest way possible for a data structure. This is because the underlying data structure that they use is an array. A value is stored at an array index determined by plugging the key into a hash function.

In Python we don’t have an array data structure that uses a contiguous block of memory. We are going to simulate an array by creating a list and keeping track of the size of the list with an additional integer variable. This will allow us to design something that resembles a hash map. This is somewhat elaborate for the actual storage of a key-value pair, but it helps to remember that the purpose of this lesson is to gain a deeper understanding of the structure as it is constructed. For real-world use cases in which a key-value store is needed, Python offers a built-in hash table implementation with dictionaries.
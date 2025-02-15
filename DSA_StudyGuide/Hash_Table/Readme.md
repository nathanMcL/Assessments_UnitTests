# Data Structures and Algorithms Study Guide

## Hash Table

Not to be confused with a `Hash Key` or properly called a `cryptographic key` used for encrypting and hashing algorithms to secure information. <br>

A `Hash Table` is a function that maps input data (*keys*) to a fixed-size integer, which determines where the data is stored
in a `hash table`.

### Basic `Hash Table` Function Examples

1. Inserting a Key-Value Pair `insert`

```
hash_table = {}
hash_table["Pikachu"] = "Electric"
print(hash_table)  
```

...Output...

```
{'Pikachu': 'Electric'}
```

2. Accessing a Value (get)

```
print(hash_table.get("Charmander", "Not Found"))
```

## Hash Table Operations

```
Operation          |  Description                |  Example
______________________________________________________________________________________________________
                   | - Adds a `key-value` pair   | `hash_table["Pikachu"] = "Electric"`
Insert(put)        | to the *table*.             |
______________________________________________________________________________________________________
                   | - Retrieves the value       | `hash_table.get("Pikachu)`
Access(get)        | associated with a key.      |
______________________________________________________________________________________________________
                   | - Modifies an existing      | `hash_table["Pikachu"] = "Thunder"`
Update(put)        | key's value.                |
______________________________________________________________________________________________________
                   | - Removes a `key-value`     | `del hash_table["Pikachu"]` or
Delete(remove)     | pair.                       | `hash_table.pop("Pikachu")`
______________________________________________________________________________________________________
                   | - Checks if a key is in     | `"Pikachu" in hash_table`
Contains(exists)   | the *table*                 |
______________________________________________________________________________________________________
                   | - Returns a list of         | `hash_table.keys()`
Keys(all_keys)     | *all keys*.                 |
______________________________________________________________________________________________________
                   | - Returns a list of         | `hash_table.values()`
Values(all_values) | *all values*.               |
______________________________________________________________________________________________________
                   | - Returns *key-value*       | `hash_table.items()`
Items(all_pairs)   | *pairs*                     |
_______________________________________________________________________________________________________
                   |                             |
Get Default        | - Gets *value* or *default* | `hash_table.get("Mewtwo", "Not Found")`
(get_or_default)   | if not found.               |
_______________________________________________________________________________________________________
                   |                             |
Clear(reset)       | - Removes `all entries`     | `hash_table.clear()`
_______________________________________________________________________________________________________
                   |                             |
Pop()              | - Removes by `key`          | `hash_table.pop("Pikachu")`
_______________________________________________________________________________________________________
                   |                             |
Get()              | - Look up a `key`           | `hash_table.get("Charmander")`
```



























































- **Big`O` Runtime**:  
  - **Access/Search**: `O(1)` (average), `O(n)` (worst-case with collisions).  
  - **Insertion/Deletion**: `O(1)` (average), `O(n)` (worst-case with collisions).  

- **Use Cases**:  
  - Fast lookups by key, such as dictionaries or caches.  
  - Managing unique sets of data like usernames or IDs.  
  - Counting occurrences of elements in a dataset.
# Data Structures and Algorithms Study Guide

## `Array.py`

An `Array` is a linear data structure consisting of a collection of elements `[...]`, where each element is identified by its index. <br>
`Arrays` store elements of the same data type in adjacent memory locations, enabling efficient random access. <br>


... Make me Understand...🙃<br>

First we want to be able to `access` the test files. <br>

```
# import required
import re
### Read the array data from the test files 
def read_array_file(file_path, pattern_to_exclude):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            # Use regex to exclude lines that are not character names (Section headers)
            return [line.strip() for line in lines if not re.match(pattern_to_exclude, line.strip())]    
    except FileNotFoundError:
        print(f"Error: File at {file_path} not found.")
        return []
```

...Next... <br>
We have to know what it is that we are wanting to do... <br>
Do we want to: <br>

1. `insert` `Charmander` into the first index position `0`of the `array_Pokemon_input` test file: Insert `Charmander` at position `0`. <br>

- What then Happens to `Pikachu`? <br>
 No worries, `Pikachu` will be moved to index `1`, and all subsequent elements will shift. <br>

- Do `Charmander` and `Pikachu` swap locations?<br>
No, `Charmander` is inserted at index `0`, and the rest of the array is shifted.

```
pokemon_array.insert(0, "Charmander")
    print(f"After inserting 'Charmander' at index 0: {pokemon_array}\n")
```
... Command Driven...<br>

```
            if operation == "insert":
                index = int(command[1])
                element = command[2]
                pokemon_array.insert(index, element)
                print(f"Inserted '{element}' at index {index}.")
```
`insert i e`<br>
Command/Index Location/Element Name  <br>
`insert 0 Bulbasaur`

2. `remove` `Charmander`: Delete the first occurrence of `Charmander`. <br>

```
if "Charmander" in pokemon_array:
        pokemon_array.remove("Charmander")
        print(f"After removing 'Charmander': {pokemon_array}\n")
    else:
        print("'Charmander' not found in the array.")
```
... Command Driven...<br>

```
            elif operation == "remove":
                element = command[1]
                pokemon_array.remove(element)
                print(f"Removed first occurrence of '{element}'.")
```
`remove e`<br>
Command/Character Name  <br>
`remove Charmander` <br>

3. `append e`: Insert `Charmander` at the Top of the Pokémon OGs list. <br>

```
pokemon_array.append("Charmander")
    print(f"After appending 'Charmander': {pokemon_array}\n")
```

... Command Driven...<br>

```
            elif operation == "append":
                element = command[1]
                pokemon_array.append(element)
                print(f"Appended '{element}' to the array.")

```

`append e` <br>
Command/Element Name <br>
`append Butterfree` <br>


4. `sort`: Sort the Pokémon OGs list alphabetically. <br>

```
pokemon_array.sort()
    print(f"After sorting alphabetically: {pokemon_array}\n")
```

... Command Driven...<br>

```
            elif operation == "sort":
                pokemon_array.sort()
                print("Sorted the Pokémon array alphabetically.")
```
Command: `sort` <br>


5. `pop`: Pop the last element from the new sorted Pokémon OGs list and print the character name. <br>

```
popped_element = pokemon_array.pop()
    print(f"Popped Element: {popped_element}")
    print(f"Array after popping the last element: {pokemon_array}\n")
```

... Command Driven...<br>

```
            elif operation == "pop":
                popped_element = pokemon_array.pop()
                print(f"Popped last element: {popped_element}.")
```

Command: `pop` <br>

6. `reverse`: Reverse the list order. <br>

```
pokemon_array.reverse()
    print(f"After reversing: {pokemon_array}\n")
    print(f"\n")
```

... Command Driven...<br>

```
            elif operation == "reverse":
                pokemon_array.reverse()
                print("Reversed the Pokémon array.")
```
Command: `reverse` <br>

7. `restore`/ "reset": Restore the original order of the Pokémon array <br>

This is not a necessary step. I added it because, what if a mistake was made along the way and it would be best to start over. <br>
How could I do that.?. <br>
Basically we are dynamically saving the current state of the `Pokémon array` in temporary memory when it creates the copy. <br>
I wouldn't consider this a `Data Structure` "Topic". I wanted to know what would have to happen...<br>

- Lines: `36/37` <br>

```
# Save the original order of the Pokémon array test file.
    original_pokemon_array = pokemon_array.copy()
```

- Lines: `125/126`<br>

```
# 7. Restore the original order of the Pokémon array
pokemon_array = original_pokemon_array
    print(f"Restored to original order: {pokemon_array}\n")
```
... Command Driven...<br>

```
            elif operation == "reset":
                pokemon_array = original_pokemon_array.copy()
                print("Restored the Pokémon array to its original order.")
```

Command: `reset` <br>

Permanently save the changes or restore the file to its original state after program execution. We are `writing back` to the file. <br>

- Lines: `128/132` <br>

```
# Optional: Write the original array back to the file after all manipulations are done.
    # This can be commented out. Purely Optional.
    with open(pokemon_filepath, 'w') as file:
        file.write('\n'.join(original_pokemon_array))
    print(f"Original order saved back to the file: {pokemon_filepath}")
```

### Big`O` Runtime

```
Operation:	Time Complexity:  Explain:  
Access	          O(1)            Direct access to an array element by index is constant time because the way arrays are implemented.
Search	          O(n)            Searching requires scanning the entire array (in the worst case) to locate the desired element.
Insertion	  O(n)            Inserting at an arbitrary index shifts all subsequent elements, leading to linear time complexity.
Deletion	  O(n)            Deleting an element also shifts elements, making it a linear operation.
Append	          O(1)*	          Adding to the end is constant time if the array has enough capacity; otherwise, resizing occurs.
Sort	          O(n log n)	  Sorting uses comparison-based algorithms (like Timsort in Python) with a typical complexity of O(n log n).
Pop	          O(1) or O(n)	  Popping the last element is O(1), but removing from the middle requires shifting, making it O(n).
Reverse	          O(n)	          Reversing involves swapping elements in place, which is linear in time complexity.
```

<br>

### Use Cases:   <br>

- Efficient to Random Access: Ideal when the position of elements is known and frequently accessed. <br>
- Storing Data (Uniformed, Consistent, Similar): For fixed-size datasets like game character stats, emoji collections, or leaderboard scores. <br>
- Visual Representations: `Arrays` are useful for static lists that are displayed in user interfaces. <br>

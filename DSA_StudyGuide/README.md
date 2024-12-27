# Data Structures and Algorithms Study Guide

I want to create a basic Data Structures and Algorithms study guide. 😄 <br>

Online coding challenges can be frustrating—sometimes they feel vague, incomplete, or poorly designed. On top of that, some require payment without much assurance of value. In my recent experience, I managed to pass single test cases but struggled to get all test cases accepted. For one challenge, I hit a wall with 9 out of 15 test cases passing. No terminal, no debugging tools—just me and a lot of guessing. 🥴 <br>

So, I’ve decided to tackle this head-on! This study guide will include programs that simulate multiple test cases to build a deeper understanding of data structures and algorithms. My goal is to not just solve problems but also to understand why certain methods work better than others. It’s time to ditch the uncertainty. Let’s do this! 🤓💪 <br>

## Set Up

Using these test files: <br>
`array_Pokemon_input.txt` <br>
`array_Emoji_input.txt` <br>
Located in this sub-directory: <br>
`myAssessment\DSA_StudyGuide\DSA_Text_files\array_testFile_input.txt` <br>
Using the Python scripts: <br>
`Array.py` <br>

## `Array.py`

An `Array` is a linear data structure consisting of a collection of elements `[...]`, where each element is identified by its index. <br>
`Arrays` store elements of the same data type in adjacent memory locations, enabling efficient random access. <br>


... Make me Understand...🙃<br>

First we want to be able to `access` the test files. <br>

```
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

- If `Charmander` were a new entry to the test file at `index` `0`, would `Pikachu` be shuffled lower on the list?<br>

```
pokemon_array.insert(0, "Charmander")
    print(f"After inserting 'Charmander' at index 0: {pokemon_array}\n")
```

2. `remove` `Charmander`: Delete the first occurrence of `Charmander`. <br>

```
if "Charmander" in pokemon_array:
        pokemon_array.remove("Charmander")
        print(f"After removing 'Charmander': {pokemon_array}\n")
    else:
        print("'Charmander' not found in the array.")
```

3. `append e`: Insert `Charmander` at the Top of the Pokémon OGs list. <br>

```
pokemon_array.append("Charmander")
    print(f"After appending 'Charmander': {pokemon_array}\n")
```

4. `sort`: Sort the Pokémon OGs list alphabetically. <br>

```
pokemon_array.sort()
    print(f"After sorting alphabetically: {pokemon_array}\n")
```

5. `pop`: Pop the last element from the new sorted Pokémon OGs list and print the character name. <br>

```
popped_element = pokemon_array.pop()
    print(f"Popped Element: {popped_element}")
    print(f"Array after popping the last element: {pokemon_array}\n")
```

6. `reverse`: Return the list back to its original order. <br>

```
pokemon_array.reverse()
    print(f"After reversing: {pokemon_array}\n")
    print(f"\n")
```

7. `restore`: Restore the original order of the Pokémon array <br>

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
Access	      O(1)            It is `Constant time`, as the `array` is indexed.
Search	      O(n)            It is `Linear time`, because every `[element]` must be checked.
Insertion	  O(n)            This requires shifting elements, making the complexity `O(n)`.
Deletion	  O(n)            Also requires shifting elements, making the complexity `O(n)`.
```
<br>

### Use Cases:   <br>

- Efficient to Random Access: Ideal when the position of elements is known and frequently accessed. <br>
- Storing Data (Uniformed, Consistent, Similar): For fixed-size datasets like game character stats, emoji collections, or leaderboard scores. <br>
- Visual Representations: `Arrays` are useful for static lists that are displayed in user interfaces. <br>


## Linked List

- Big`O` Runtime: <br>

- Use Cases:   <br>

## Tree (Tree, Binary Tree, Binary Search Tree, Red-Black Tree, etc.)

`Tree`:   <br>

- Big`O` Runtime:  <br> 

- Use Cases:   <br>

`Binary Tree`:   <br>

- Big`O` Runtime:  <br> 

- Use Cases:   <br>

`Binary Search Tree`:   <br>

- Big`O` Runtime:  <br> 

- Use Cases:   <br>

`Red-Black Tree`:   <br>

- Big`O` Runtime:  <br> 

- Use Cases:   <br>

## Heap

- Big`O` Runtime:    <br>

- Use Cases:   <br>

## Hash Table

- Big`O` Runtime:     <br>

- Use Cases:   <br>

## Stack

- Big`O` Runtime:     <br>

- Use Cases:   <br>

## Queue

- Big`O` Runtime:    <br>

- Use Cases:   <br>

## Tree

- Big`O` Runtime:    <br>

- Use Cases:   <br>

## Graph (both directed and undirected)

- Big`O` Runtime:   <br>

- Use Cases:   <br>

## Algorithms


## Sorting: 

- `Bubble Sort`


- `Merge Sort`


- `Quick Sort`


- `Radix / Bucket Sort`



## Traversals with multiple data structures

- `Depth First Search`
- `Breadth First Search`

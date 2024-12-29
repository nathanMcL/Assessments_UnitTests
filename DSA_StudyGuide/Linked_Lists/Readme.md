# Data Structures and Algorithms Study Guide

(*TODO* Link the wiki links to the individual `highlighted` terminology: `Linked List`, `node`, `linear data structure`...etc) <br>
Wiki Link: https://en.wikipedia.org/wiki/Node_(computer_science)<br>

---

## Set Up

Using these test files: <br>
`Emoji_description.txt` <br>
`array_Emoji_input.txt` <br>

Located in this sub-directory: <br>
`myAssessment\DSA_StudyGuide\DSA_Text_files\array_testFile_input.txt` <br>

Using the Python script: <br>
`Linked_Lists.py`<br>

---

## Linked Lists

So, what is a linked list... well, a linked list could be as simple as two text1.txt and text2.txt files created from your note pad on your device...<br>
The `Linked_Lists.py` script is a command-driven Python program designed to demonstrate how linked lists using fun and practical examples:<br>

- Merging: `merge` emoji descriptions with their corresponding emoji icons. <br>
- Reversing: `reverse` the order of the linked lists.
- Comparing: `compare` the linked lists node structure data.

---

### What is Happening in the Code?

- 1. **Understanding the Linked List Structure**:
- A `Linked List` in programming is a `linear` `data structure` where data is stored in individual `nodes`. <br>
- Each **emoji** (icon 😬) and its **description** (Awkward) are treated as `nodes`.<br>

1. What is a `node`? <br>

A node is a basic unit of a data structure, such as a `linked list` or `tree` data structure. <br>
`Nodes` contain data <br>

2. **Data**: The `emoji icon` or `emoji description`<br>

```
[
Weather  Description
☀️       Sunny  
☁️
🌈
☂️
]
```
and may also link to other nodes...<br>
...ok...but...How.?. <br>

- `Link Lists` are linked togeather using `pointers`. <br>

1. What is a `pointer`?<br>

A `pointer` is a special variable within each `node` that stores the memory address of the next node in the sequence.<br>

Each `node` contains two parts: the data and the reference or `pointer` to the next node in the sequence. <br>

- The `data` like an 👽 or its description `Alien`.<br>
👾 - `Game alien`, 🤖 - `Robot`, 👻 - `Ghost`...<br>

...code...<br>

```
# Each emoji description and Icon are stored as an individual Node.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### Advatages of Linked Lists:

1. **Dynamic Size**: Can grow or shrink in size without the need for resizing arrays.<br>
2. **Efficient Insertions/Deletions**: Insertions and deletions can be performed efficiently in constant time, `0(1)`, if the pointer to the location is know. <br>

### Limitations:

1. **Sequential Access**: Accessing elements requires traversing the list, making the time complexity for search operations `0(n)`.<br>
2. **Overhead**: Requires extra memory for pointers. <br>


Building upon our `Array` accessing framework, we will now attempt to manipulate the Test file lists. Not the list itself...<br>  

---

## Key Operations

### Creating Linked Lists

- The `create_linked_list` function dynamically builds linked lists by adding `nodes` for each emoji 😺 or description `Cat face`. <br>

### Merge Sorted Linked Lists

- **Description**: Combine two sorted linked lists into a single sorted linked list with the `Emoji Description` spaced beside the `Emoji` Icon.<br>
- 1. The `merge_with` method combines two linked lists into a single list where each emoji icon is paired with its corresponding emoji decription. <br>

- What if one list has more elements than the other? <br>
If the list do not have the same amount of elements, or if list # 1 has 10 elements and list # 2  has 8 element, the extra `nodes` are appended (added to the end of) to the merged list.<br>


```
[
    🐶
    🦊
    🐻
    🐼
]
```
`merge_with` <br>
```
[
    Dog face
    Fox face
    Bear face
    Panda face
]
```

### Merge the two lists: `array_Emoji_input.txt` and `Emoji_description.txt`<br>

**Whats the code?** <br>

- There are two `pointers`, `p1` and `p2`, start at the heads (or top of the two lists) of the two `linked lists`. <br>
- While both `pointers` have `nodes`:

1. Create a `new node` by combining the data from `p1` and `p2` ("😀 - Happy Face").
2. Add this `new node` to the `merged` list.
3. Move both `pointers` to the `next node` in their respective lists.<br>

- Once one list is exhausted, any remaining `nodes` from the other list are `appended` to the merged list. <br>

```
    def merge_with(self, other):
        merged = LinkedList()
        p1 = self.head
        p2 = other.head

        while p1 and p2:
            merged.append(f"{p1.data} - {p2.data}")
            p1 = p1.next
            p2 = p2.next

        # Append the remaining nodes from either list
        while p1:
            merged.append(p1.data)
            p1 = p1.next
        while p2:
            merged.append(p2.data)
            p2 = p2.next

        return merged
```

### Merge the two lists: Operation Command `merge`

```
        if operation == "merge":
            self.merged_ll = self.emoji_ll.merge_with(self.description_ll)
            print(f"Merged '{self.emoji_array_filepath}' & '{self.emoji_description_path}'.\n")
            self.merged_ll.display()
```

### Displaying the `Merged` Lists

- The `display` method traverses the merged linked list, `node` by `node` and prints the data in each node sequentially.<br>  

**Whats the code?** <br>

- A `pointer`, **current**, starts at the head of the linked list.<br>
- While `current` is not `None` (meaning there are still `nodes` to process): 
- 1. Print the data in the `current node`.<br>
- 2. Move the pointer to the `next node`.<br>

```
# Display the list
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
```

#### Why use this?

- To visually confirm the structure and contents of the linked list. <br>
- This is useful for debugging or simply understanding how the data is stored in the list.<br>

- **Runtime Complexity**: `O(n + m)` where `n` and `m` are the lengths of the two lists.
- **Use Case**: Useful in scenarios like merging data streams or when sorting datasets using divide-and-conquer techniques. <br>

### Reverse a Linked List

- **Description**: 
The `reverse` method changes the order of the nodes `(Emojis)` in the linked lists. (A...Z to Z...A)

### Reverse the combined Linked Lists

**Whats the code?** <br>

- Three `pointers`, `prev`, `current`, and `next_node`, are used: <br>

1. Start with `prev` as `None` and `current` pointing to the `head` of the list.<br> 

2. For each `node`:<br>

- Save the next `node` in `next_node`. <br>
- Reverse the direction of the `next` `pointer` so it points to `prev`.<br>
- Move `prev` to `current` and `current` to `next_node`.

3. When the traversal is complete, `prev` will point to the new head of the reversed list. <br>


```
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
```

### Reverse the merged lists order: Operation Command `reverse`

```
        elif operation == "reverse":
            if self.merged_ll:
                self.merged_ll.reverse()
                print("Reversed the order of the Linked Lists:")
                self.merged_ll.display()
            else:
                print("No merged list to reverse. Use the 'merge' command first.")
```

- **Runtime Complexity**: `O(n)`.
- **Use Case**: Frequently used in algorithms like palindrome detection in linked lists or reversing sequences for processing. <br>

### Compare Two Linked Lists

- **Description**: Check if two linked lists are identical in terms of node data and structure. There should be one Description for each individual Emoji Icon.<br>
- **Runtime Complexity**: `O(n)` where `n` is the smaller of the two list sizes.
- **Use Case**: Useful for data validation or ensuring data consistency across two linked structures. <br>

---

### Big`O` Runtime for Linked Lists: <br>

```
Access: 0(n) - Traversal is required to access elements.
Search: 0(n) - Each element must be checked sequentially.
Insertion: 0(1) - Constant time if the insertion point is known.
Deletion: 0(1) - Constant time if the deletion point is known.
```

### Use Cases:   <br>

- Dynamic Data Management: Ideal for implementing `stacks`, `queues`, and `adjacency lists` for graphs.
- Memory Efficiency: Suitable for environments where memory allocation patterns are unpredictable.
- Scenarios with Frequent Insertions/Deletions: Common in real-time systems, operating systems, or undo features in software. <br>

---

**Noted Sources**:

- https://docs.python.org/3/tutorial/datastructures.html <br>
- https://docs.python.org/3/library/collections.html#collections.deque <br>

---

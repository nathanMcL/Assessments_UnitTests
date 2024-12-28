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
- 1. The `merge_with` method combines two linked lists into a single list where each emoji icon is paired with its corresponding decription:

```
🐶 - Dog face
🦊 - Fox face
🐻 - Bear face
🐼 - Panda face
```

### Displaying the `Merged` Lists

- The `display` method traverses the merged list and prints each node sequentially.  

- **Runtime Complexity**: `O(n + m)` where `n` and `m` are the lengths of the two lists.
- **Use Case**: Useful in scenarios like merging data streams or when sorting datasets using divide-and-conquer techniques. <br>

### Reverse a Linked List

- **Description**: Reverse the order of the nodes `(Emojis)` in the linked lists.
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



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

So, what is a linked list... well, a linked list could be as simple as two files (`text1.txt` and `text2.txt`) created from your note pad on your device...<br>
The `Linked_Lists.py` script is a command-driven Python program designed to demonstrate how linked lists can work while using fun and practical examples:<br>

- **Merging**: `merge` emoji descriptions with their corresponding emoji icons.  
- **Reversing**: `reverse` the order of the linked lists.  
- **Comparing**: `compare` the linked lists' node structure and data.

---

### What is Happening in the Code?

#### 1. **Understanding the Linked List Structure**:

A `Linked List` in programming is a `linear` `data structure` where data is stored in individual `nodes`. <br>
Each **emoji** (icon 😬) and its **description** (Awkward) are treated as `nodes`.<br>

#### 2. **What is a `node`?** <br>

A node is a basic unit of a data structure, such as a `linked list` or `tree`. Nodes contain **data** (like an emoji icon or description). <br>

#### 3. **How are Nodes Linked?**

Nodes in linked lists are connected using **pointers**: <br>

- A `pointer` is a special variable within each `node` that stores the memory address of the next node in the sequence.<br>

Each `node` contains two parts: <br>

1. **Data**: The emoji (👽) or its description (`Alien`). <br>
2. **Pointer**: A reference to the next node.

```
Node 1 [☀️] -> Node 2 [☁️] -> Node 3 [🌈] -> Node 4 [☂️] -> None
```

**Code Example** <br>

```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

---

### Advatages of Linked Lists

1. **Dynamic Size**: Can grow or shrink in size without the need for resizing arrays.<br>
2. **Efficient Insertions/Deletions**: Insertions and deletions can be performed efficiently in constant time, `0(1)`, if the pointer to the location is know. <br>

### Limitations:

1. **Sequential Access**: Accessing elements requires traversing the list, making the time complexity for search operations `0(n)`.<br>
2. **Overhead**: Requires extra memory for pointers. <br>


Building upon our `Array` framework, we will now attempt to `access`, `merge`, `reverse`, `compare`, and `save` a linked list.<br>  

---

## Key Operations

### Creating Linked Lists

The `create_linked_list` function dynamically builds linked lists by adding `nodes` for each emoji 😺 or description `Cat face`. <br>

### Merge Sorted Linked Lists

#### **Description**:

 Combine two sorted linked lists into a single sorted linked list with the `Emoji Description` spaced beside the `Emoji` Icon.<br>

- 1. The `merge_with` method combines two linked lists into a single list where each emoji icon is paired with its corresponding emoji decription. <br>

- What if one list has more elements than the other? <br>
If the list do not have the same amount of elements, or if list # 1 has 10 elements and list # 2  has 8 element, the extra `nodes` are appended (added to the end of) to the merged list.<br>

#### Before Merging:<br>

Linked List # 1:<br>
```
[
    🐶
    🦊
    🐻
    🐼
]
```
`merge_with` <br>
Linked List # 2:<br>
```
[
    Dog face
    Fox face
    Bear face
    Panda face
]
```

### Merge the two lists: `array_Emoji_input.txt` and `Emoji_description.txt`<br>

**What's the code?** <br>

- There are two `pointers`, `p1` and `p2`, start at the heads (or top of the two lists) of the two `linked lists`. <br>
- While both `pointers` have `nodes`:

1. Create a `new node` by combining the data from `p1` and `p2` ("😀 - Happy Face").
2. Add this `new node` to the `merged` list.
3. Move both `pointers` to the `next node` in their respective lists.<br>

- Once one list is exhausted, any remaining `nodes` from the other list are `appended` to the merged list. <br>

#### Code:

```
    def merge_with(self, other):
        merged = LinkedList() # Create a new merged linked list
        p1 = self.head        # Pointer for the first list.
        p2 = other.head       # Pointer for the second list.

        # Traverse both lists simultaneously.
        while p1 and p2:
            merged.append(f"{p1.data} - {p2.data}") # Combine and append data.
            p1 = p1.next                            # Move the pointer to the next node in list #1.
            p2 = p2.next                            # Move the pointer to the next node in list #2.

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

**What's the code?**
```
        if operation == "merge":
            self.merged_ll = self.emoji_ll.merge_with(self.description_ll)
            print(f"Merged '{self.emoji_array_filepath}' & '{self.emoji_description_path}'.\n")
            self.merged_ll.display()
```

### Displaying the `Merged` Lists

- The `display` method traverses the merged linked list, `node` by `node` and prints the data in each node sequentially.<br>  

**What's the code?** <br>

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

#### After Merging:

```
[🐶 - Dog face -> 🦊 - Fox face -> 🐻 - Bear face -> 🐼 - Panda face]
```

#### Why use this?

- To visually confirm the structure and contents of the linked list. <br>
- This is useful for debugging or simply understanding how the data is stored in the list.<br>

- **Runtime Complexity**: `O(n + m)` where `n` and `m` are the lengths of the two lists.
- **Use Case**: Useful in scenarios like merging data streams or when sorting datasets using divide-and-conquer techniques. <br>

### Reverse a Linked List

#### **Description**: <br>

The `reverse` method changes the order of the nodes `(Emojis)` in the linked lists. (A...Z to Z...A)

### Reverse the combined Linked Lists

**What's the code?** <br>

- Using `pointers`, `prev`, `current`, and `next_node` are used: <br>

1. Start with `prev` as `None` and `current` pointing to the `head` of the list.<br> 

2. For each `node`:<br>

- Save the next `node` in `next_node`. <br>
- Reverse the direction of the `next` `pointer` so it points to `prev`.<br>
- Move `prev` to `current` and `current` to `next_node`.

3. When the traversal is complete, `prev` will point to the new head of the reversed list. <br>

#### Code:

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

#### Code:

```
        elif operation == "reverse":
            if self.merged_ll:
                self.merged_ll.reverse()
                print("Reversed the order of the Linked Lists:")
                self.merged_ll.display()
            else:
                print("No merged list to reverse. Use the 'merge' command first.")
```

#### Reverse Example: <br>

```
Before Reversing: [A -> B -> C -> D -> None]
After Reversing:  [D -> C -> B -> A -> None]
```

- **Runtime Complexity**: `O(n)`. <br>
- **Use Case**: Frequently used in algorithms like palindrome detection in linked lists or reversing sequences for processing. <br>

---

### Compare Two Linked Lists

#### **Description**: <br>

Check if two linked lists are identical in terms of node data and structure. There should be one Description for each individual Emoji Icon.<br>

**What's the code?** <br>

1. In this section we want to `compare` that the `emoji` linked list has a `description` for each emoji icon.<br>
2. `While` `comparing` the data, the node data individually might not be the same, so we should also strip the leading and trailing whitespaces.<br>
3. If the lists are not the same length, that could mean one has extra nodes.<br>

#### Code:

```
    def compare_with(self, other):
        p1 = self.head
        p2 = other.head

        while p1 and p2:
            if p1.data.strip() != p2.data.strip():
                return False
            p1 = p1.next
            p2 = p2.next

        return p1 is None and p2 is None
```
...Next in `comparing`...<br>

*`Validate`* that the Merged Linked List is aligned with the Combined Linked List elements.<br>

1. In the `validate_merged_ll` method we traverse the `merged_ll` list (*`current`* `pointer`) and we are compare each node's `data` with the corresponding item in the `combined_list`.<br>
2. If any mismatch is found or if the lengths differ, it returns `False`.<br>
3. If all items match, it confirms the merged list is valid by returning `True`.<br> 

#### Code:

```
    def validate_merged_ll(self, combined_list):
        current = self.head
        for item in combined_list:
            if not current or current.data.strip() != item.strip():
                return False
            current = current.next
        return current is None
```

...*Side Note*...<br>
Comparing a pair of linked lists is a takes a different approach...<br>
We arn't just comparing that there is a description for each emoji. We are comparing the actual data within the tests files to compare that the data is the same in each test file. <br>
Since the Test files data are different you would receive an error message.<br>
We would need to compare the merged list against the expected combined list.<br>

#### Solution

The goal is to `compare` the merged list with the combined original emoji and description lists to ensure they correct:

1. Combine the `emoji_array` and `description_array` into a single list for comparison.<br>
2. Create a new method to `validate` the `merged_ll` against the combined list.<br>


- **Runtime Complexity**: `O(n)` where `n` is the smaller of the two list sizes.<br>
- **Use Case**: Useful for data validation or ensuring data consistency across two linked structures. <br>

---

### Big`O` Runtime for Linked Lists: <br>

```
| Operation   | Time Complexity | Explaination                                  |
|-------------|-----------------|-----------------------------------------------|
| Access      | `O(n)`          | Traversal is required to access elements.     |
| Search      | `O(n)`          | Each element must be checked sequentially.    |
| Insertion   | `O(1)`          | Constant time if the insertion point is known.|
| Deletion    | `O(1)`          | Constant time if the deletion point is known. |
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

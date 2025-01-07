# Data Structures and Algorithms Study Guide

## Tree Search Algorithms:

- Depth-First Search (DFS)<br>
- Breadth-First Search (BFS)<br>
- Tree<br>
- Binary Tree<br>
- Binary Search Tree<br>
- Red-Black Tree<br>

---

## Set Up

Using these test files: <br> 
`Emoji_description.txt`  <br>
`array_Emoji_input.txt`  <br>
`Merged_Emoji_LinkedList`<br>
`BST_Pokemon_color_alignment`<br>
`BST_Pokemon_Type_color_list`<br>

Located in this sub-directory:  <br>
`DSA_StudyGuide\DSA_Text_files\see_test_files.txt`  <br>

Using the Python scripts: <br>

- Main: `Tree_Searches.py`<br>
- Depth-First Search (DFS): `dfs.py`<br>
- Breadth-First Search (BFS): `bfs.py` <br>
- Tree: `tree.py` <br>
- Binary Tree: `binary_tree.py`<br>
- Binary Search Tree: `binary_search_tree.py`<br>
- Red-Black Tree: ` ` <br>


---

### `Depth-First Search (DFS)`

DFS algorithm explores a graph by starting at a chosen `node` and traversing as far down `one branch` as possible before backtracking to explore other branches, essentially *"diving deep"* into the graph until it reaches a dead end before moving on to other potential paths. <br>
The `DFS` uses a `stack` data structure to keep track of visited `nodes` and the path to backtrack to; this process continues until all reachable `nodes` in the graph have been visited.<br>

#### DFS Code Example

```
def simulate_dfs():
    print("\nSimulating Depth-First Search (DFS):")
    tree = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['G', 'H'],
        'F': [],
        'G': [],
        'H': []
    }

    def dfs(node, visited):
        if node not in visited:
            visited.append(node)
            print(f"Visited: {node}")
            for neighbor in tree[node]:
                dfs(neighbor, visited)
    
    print("Starting DFS from root node 'A':")
    visited_nodes = []
    dfs('A', visited_nodes)
    print("DFS Traversal Complete!")
```

- **Big`O` Runtime:**  
  - Time Complexity: O(V + E) where V is vertices and E is edges (for graphs).  
  - Space Complexity: O(H) where H is the height of the tree.  

- **Use Cases:**  
  - Solving puzzles like mazes or pathfinding.
  - Evaluating expressions in expression trees.

---

#### dfs.py

```
# Step 2: Create a tree from the test data
    tree = {
    icon: [desc] for icon,
    desc in zip(emoji_icons[:len(emoji_descriptions)],
    emoji_descriptions)
  }

# Step 3: Depth-First Search Function
    def dfs(node, visited, depth=0):
        if node not in visited:
            visited.append(node)
            description = tree.get(node, ['No description found'])[0]
            indent = "  " * depth
            if description == 'No description found':
                description = "default Description for Missing Data"
            indent = "  " * depth
            print(f"{indent}Visited: {node} - {description}")
            for neighbor in tree.get(node, []):
                dfs(neighbor, visited, depth + 1)
    
    # Step 4: Run DFS and display the traversal
    print("Starting DFS from root node '😀':")
    visited_nodes = []
    dfs('😀', visited_nodes)
    print("DFS Traversal Complete!")
```

#### DFS Output

```
Simulating Depth-First Search (DFS):
Starting DFS from root node '😀':
Visited: 😀 - 😂
  Visited: 😂 - 🤔
    Visited: 🤔 - Thinking
      Visited: Thinking - default Description for Missing Data
    Visited: 😎 - Cool sunglasses
      Visited: Cool sunglasses - default Description for Missing Data
  Visited: 😍 - 🥳
    Visited: 🥳 - Celebration
      Visited: Celebration - default Description for Missing Data
    Visited: 🤩 - Starstruck
      Visited: Starstruck - default Description for Missing Data
DFS Traversal Complete!
```

### `Breadth-First Search (BFS)`

The *`Breadth-First Search`* (BFS) algorithm explores a `graph` or `tree` by systematically visiting all `nodes` at the current depth level before moving on to the next level, essentially "taking off" from a starting node, ensuring it finds the shortest path to any target node by checking all nodes one "hop" away before moving to nodes further away; it uses a `queue` data structure to keep track of nodes to visit, adding neighbors of the currently visited node to the queue as they are discovered.<br>

#### BFS Code Example

```
from collections import deque

def simulate_bfs():
    print("\nSimulating Breadth-First Search (BFS):")
    tree = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['G', 'H'],
        'F': [],
        'G': [],
        'H': []
    }

    def bfs(start):
        queue = deque([start])
        visited = []
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                print(f"Visited: {node}")
                queue.extend(tree[node])
    
    print("Starting BFS from root node 'A':")
    bfs('A')
    print("BFS Traversal Complete!")

```

- **Big`O` Runtime:**  
  - Time Complexity: O(V + E) for graphs.
  - Space Complexity: O(W) where W is the maximum width of the tree.  

- **Use Cases:**  
  - Finding the shortest path in unweighted graphs.
  - Peer-to-peer networking.

---

#### BFS Output

```
Simulating a Breadth-First Search (BFS):
Starting BFS from root node '😀(A)':
Visited: 😀 - 😂
Visited: 😂 - Laughing tears
Visited: 😍 - Heart eyes
Visited: Laughing tears - Default Description for Missing Data
Visited: Heart eyes - Default Description for Missing Data
BFS Traversal Complete!
```

### `Tree`

A `tree` search algorithm works by systematically exploring the `nodes` of a tree data structure, starting at the `root node`, to find a specific node that satisfies the desired conditions of a problem, essentially navigating through the hierarchical structure of the tree to reach the solution. <br>
The `Tree` search alogrithm does this by examining *each* `child node` in a defined order, like `depth-first` or `breadth-first` search; it essentially "walks" through the tree, checking each node until it finds the target value or reaches a point where no further exploration is needed.<br>

#### How the Tree Search Algorithms Functions

Traversal Strategies:<br>

`Depth-First Search (DFS)`:<br>

1. Explores as far as possible along each branch before backtracking.<br>
2. Uses a stack (can be implicit with recursion) to keep track of nodes.<br>

`Breadth-First Search (BFS)`:<br>

1. Explores all `nodes` at the current level before moving to the next level.<br>
2. Uses a queue to manage nodes to be visited.<br>

`Goal-Based` Search Criteria: <br>

1. Looks for a specific node or value within the tree.<br>

`Exhaustive` Search: <br>

1. Visits all nodes to perform operations like summing values or checking conditions.<br>

#### Tree Code Example

```
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search(root, value):
  if root is None or root.value == value:
        return root

    if value < root.value:
        return search(root.left, value)
    else:
        return search(root.right, value)
```

#### What's the code?

Step 1: `Read` and `filter` the data from the test files. <br>

Step 2: `Build` the `Tree`: <br>

- Root Node: `Root` = 😀<br>
- 1. Level 1: First `3` `emoji icons` as `children`of the `root`.<br>
- 2. Level 2: First `6` `emoji descriptions` are distributed among `Level 1` *`nodes`*(2 children each).<br>
- 3. Level 3: First `9` `merged` emoji-description pairs as `grandchildren` (3 per level 2 child). 

Step 3: `Connect` the `Nodes`:<br>

- Links each `node`(parent-child relationship) to form the `tree` structure.<br>

Step 4: `Traverse` the `Tree`<br>

- 1. Performs a `Depth-First Traversal`.<br>
- 2. Visits each `node`, prints its value, and recursively visits its children.<br>
- 3. `Indentation` indicates the depth of the node in the structural hierarchy.<br> 

---

- **Big`O` Runtime:**  
  - Insert, Delete, Search: O(n) (worst case, unbalanced tree).  

- **Use Cases:**  
  - Representing hierarchical data such as organizational charts or file systems.

---

...*Notes*...<br>

...*Reduce Repetition*...<br>
If some `nodes` are appearing under multiple `parents`.<br>
Ensure `unique` children are created for each `parent`:<br>

- 1. Use `indices` while `slicing` data.<br>
- 2. Confirm the `nodes` are assigned only *once* during the tree construciton.<br> 

...*Output Clarity*...<br>
Label the `node` level and/or/both? `parent-child relationships`.<br>

- 1. `"Level 1: 😀"`
- 2. `"Level 2: Happy Face"`

...*Dynamic Levels*...<br>
Problem:<br>
The `tree` construction is hardcoded, using a fixed number of children (2 children per parent, 3 garndchildren per child)... That is my issue when doing the online coding challenges. I have been able to get the `"hardcoded"` portion of the challenges, thats😀great! But!!!😧 That does not allow for multiple test case files to be ran with the set code.🧐...<br> 

🤓...💡...😀<br>

Dynamically assign children based on the test data...🔥<br>

- 1. Divide children evenly across the parents.<br>
- 2. Handle cases where the number of `nodes` is not divisible evenly...🤨<br>

---

#### Tree.py Output

```
Enter a command: tree

Simulating the Tree Search Algorithm:
Starting Tree Search Traversal from 😀:
Root: Root = 😀
  Level 2: 😀
    Level 3: Happy face
      Level 4: 😀 - Happy face
      Level 4: 😂 - Laughing tears
      Level 4: 😍 - Heart eyes
    Level 3: Laughing tears
      Level 4: 🤔 - Thinking
      Level 4: 😎 - Cool sunglasses
      Level 4: 🥳 - Celebration
  Level 2: 😂
    Level 3: Heart eyes
      Level 4: 🤩 - Starstruck
      Level 4: 🥺 - Pleading face
      Level 4: 😖 - Distressed
    Level 3: Thinking
  Level 2: 😍
    Level 3: Cool sunglasses
    Level 3: Celebration
Tree Search Traversal Complete!
```
---



### `Binary Tree`

Now we are deep in a forest! A `Binary Tree` is a heirarchical data structure in which each `node` has at most `two children`:<br>

- 1. `Left Child`<br>
- 2. `Right Child`<br>

Each `child` can be either:<br>

- 1. Another `node` continuing the tree structure.<br>
- 2. `Null` indicating that `no` `child` exists in that position.<br>

The `binary tree` has a strict `two-child` rule that makes binary trees suited for applications like hierarchical representations, arithmetic computations, and certain search or traversal operations.<br>

#### Binary Tree Features

`Nodes` contain:

- 1. A value or key.<br>
- 2. A reference to the `left child`.<br>
- 3. A reference to the `right child`<br>

#### Binary Tree `types`:

1. `Full Binary Tree:` Each `node` has either `0` or `2` `children`.<br>
2. `Complete Binary Tree`: All levels are fully filled, except the last level, which is filled from left to right.<br>
3. `Balanced Binary Tree`: The difference in height between the left and right subtrees of any `node` is minimal.<br>
4. `Skewed Binary Tree`: Resembles a linked list where each parent has only one child.<br>

- **Big`O` Runtime:**  
     - Insert, Delete, Search:<br>

1. Unbalanced Binary Tree: O(n) in the worst case (resembles a linked list).<br>
2. Balanced Binary Tree: O(logn) due to reduced height.<br>

     - Traversal:<br>

1. In-Order, Pre-Order, Post-Order: O(n), as every node is visited once.  <br>

- **Use Cases:**  <br>
  - Representing arithmetic expressions.<br>
  - Organizing hierarchical data with strict binary conditions.<br>

---

#### What is the difference between a `Tree Search Algorithm`?<br>

```
Aspect:            ->                 Binary Tree                                    VS                  Tree Search Algorithms
1. Definition:     -> A specific type of tree where nodes have at most two children. vs Algorithms used to traverse or search any tree structure.
2. Purpose:        -> Structure to organize data hierarchically.                     vs Navigating or exploring trees efficiently.
3. Travel Methods: -> In-order, pre-order, post-order.                               vs DFS, BFS (general algorithms for all trees).
4. Focus:          -> Tree structure rules (left/right child).                       vs Other strategies, not limited to binary trees.

```
Key Difference:<br>
`Binary trees` define a specific `tree` structure, while `tree search` algorithms describe `methods`(dfs,bfs) for traversing any tree.<br>

---

#### Binary Representation:

```
    Level 1
      😀
    /    \
    Level 2
  😂     😍
 /  \    /  \
    Level 3
🤔  😎 🥳  🤩
```

### `binary_tree.py` code

#### Define the Binary Tree Node class.<br>

```
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

#### Display the nodes of the Binary Tree Levels

```
def display_binary_tree_levels(root):
    if not root:
        print("Binary Tree is empty.")
        return
    queue = deque([(root, 0)])
    (node, level)
    current_level = 0
    level_nodes = []

    print("\nBinary Tree Level-Based Output:")
    while queue:
        node, level = queue.popleft()
        if level > current_level:
            print(f"Level {current_level + 1}: {', '.join(level_nodes)}")
            level_nodes = []
            current_level = level
        level_nodes.append(node.value)
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    # Print the last level
    if level_nodes:
        print(f"Level {current_level + 1}: {', '.join(level_nodes)}")
```

#### Display the Binary Tree Parent-Child relationships

```
def display_BTPC_relationships(root):
    if not root:
        print("Binary Tree is empty.")
        return
    
    print("\nBinary Tree Parent-Child Relationships:")
    queue = deque([root])
    while queue:
        node = queue.popleft()
        left_child = node.left.value if node.left else "None"
        right_child = node.right.value if node.right else "None"
        print(f"Parent: {node.value}, Left Child: {left_child}, Right Child: {right_child}")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

#### Simulate the Binary Tree Search Algorithm

```def simulate_binary_tree():```

#### Step 1: Load the test data

```
 base_dir = os.path.dirname(os.path.abspath(__file__))
    binarytree_description_path = os.path.join(base_dir, "../DSA_Test_files/BinaryTree_Descriptions_Input.txt")
    binarytree_emoji_icons_path = os.path.join(base_dir, "../DSA_Test_files/BinaryTree_Emoji_Input.txt")
```

#### Step 2: Combine test data for nodes

```
    combined_values = [f"{emoji} - {desc}" for emoji, desc in zip(binarytree_emoji_icons[:len(binarytree_descriptions)], binarytree_descriptions)]
```

#### Step 3: Build the Binary Tree

```
    root = build_binary_tree(combined_values)
```

#### Step 4: Display the Binary Tree Level-Based Ouput
    
```
    display_binary_tree_levels(root)
```

#### Step 5: Display the Bonary Tree Parent-Child Relationships

```
    display_BTPC_relationships(root)
```

#### The End...

```
    print("Binary Tree Traversal Complete!")
```

#### `binary_tree.py` output

```
Simulating the Binary Tree Search Algorithm:

Binary Tree Level-Based Output:
Level 1: 😾 - Pouting cat
Level 2: 😿 - Crying cat, 🙀 - Scared cat
Level 3: 😽 - Kissing cat, 😼 - Smug cat, 😻 - Love-struck cat (heart eyes), 😹 - Laughing cat (tears of joy)
Level 4: 😸 - Grinning cat, 😺 - Happy cat

Binary Tree Parent-Child Relationships:
Parent: 😾 - Pouting cat, Left Child: 😿 - Crying cat, Right Child: 🙀 - Scared cat
Parent: 😿 - Crying cat, Left Child: 😽 - Kissing cat, Right Child: 😼 - Smug cat
Parent: 🙀 - Scared cat, Left Child: 😻 - Love-struck cat (heart eyes), Right Child: 😹 - Laughing cat (tears of joy)
Parent: 😽 - Kissing cat, Left Child: 😸 - Grinning cat, Right Child: 😺 - Happy cat
Parent: 😼 - Smug cat, Left Child: None, Right Child: None
Parent: 😻 - Love-struck cat (heart eyes), Left Child: None, Right Child: None
Parent: 😹 - Laughing cat (tears of joy), Left Child: None, Right Child: None
Parent: 😸 - Grinning cat, Left Child: None, Right Child: None
Parent: 😺 - Happy cat, Left Child: None, Right Child: None
Binary Tree Traversal Complete!
```

---

...*Notes*...<br>
Improvements:

1. Highlight `Leaf` Nodes:
    - Add a marker for `nodes` with children to indicate they are leaf nodes explicity...<br>
    
```
Parent: 😸 - Grinning cat (Leaf Node), Left Child: None, Right Child: None
```

2. Be able to "step-through" the `parent-child` relationships interactively, to observe each node's connection in real time, not just printed out at once...<br>

---



## `Binary Search Tree (BST)`

A `Binary Search Tree` (*`BST`*) is a specialized form of the `Binary Tree`.<br>
This `binary tree` ensures its `nodes` are stored in a way that allows for efficient: `searching`, `insertion`, and `deletion`.<br>

### BST Rules

1. `Left Subtree`: Contains only `nodes` with values less than the `parent` `node's` value.<br>
2. `Right Subtree`: Contains only `nodes` with values `greater` than the `parent` `node's` value.<br>
3. `No Duplicates`: Duplicate `nodes` are not allowed in a `BST`.<br>

### BST Features

1. `Dynamic Sorted Structure`: Unlike `arrays` or `linked lists`, `BSTs` dynamically maintain `sorted order`.<br>
2. `Hierarchical Organization`: `Nodes` are organized into `parent-child` relationships, ensuring fast lookup times for balanced trees.



---

- **Big`O` Runtime:**  
  - Insert, Delete, Search: O(log n) (average), O(n) (worst case, unbalanced). 

#### Operations and Their Runtimes

```
Operation ->	Average Case ->	Worst Case (Unbalanced Tree) ->	Explanation
Search    -> 	  O(log n)   ->        O(n)                  -> Tree height determines performance; log n for balanced trees, linear for unbalanced.
Insert	  ->  O(log n)	   ->        O(n)	                 -> Similar to search as the tree grows dynamically.
Delete	  ->  O(log n)	   ->        O(n)	                 -> Involves locating and rearranging nodes.
```

#### Use Cases:

1. Dynamic Searching: Efficient for dynamically updating data sets while preserving sorted order.<br>
2. Set Implementations: Useful for implementing sets and multisets.<br>
3. Database Indexing: Often used in databases for indexing records due to its ordered nature. <br>

---

#### BST Example

```
  Level 1
    50
   /  \
  Level 2
Left  Right  
  30   70
 / \   / \
  level 3
20 40 60 80
```

Left side values are less than the right side's values.<br>

#### Defining the BST Node class:

```
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

#### Insert Function:

```
def insert(root, value):
    if root is None:
        return BSTNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root
```

#### Search Function:

```
def search(root, value):
    if root is None or root.value == value:
        return root
    if value < root.value:
        return search(root.left, value)
    return search(root.right, value)
```

#### Delete Function:

```
def delete(root, value):
    if root is None:
        return root
    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = find_min(root.right)
        root.value = temp.value
        root.right = delete(root.right, temp.value)
    return root

def find_min(node):
    while node.left:
        node = node.left
    return node
```

...`Notes`...*<br>

ok, the binary search tree is almost like the least-to-greatest filter option.<br>

Currently(1/2/25) Attempting to create a visual representation is challenging.<br>

There are a couple of issues...<br>

  - I need to move on and work on understanding the next section... `:(`<br>

  - Learning to use the `binarytree` library with my data.

  - Learning how to utilize `matplotlib.plyplot`. I thought, that because of the `BST level-based output`, when printed to the terminal, some of the mapped data overlaps the other node data and does not make sense. So, *`note`* to future self, Using matplotlib(*and* HTML, Text, JSON), `I` = `you` wants to be able to save the BST level-based output such that the `entire` *`Binary Search Tree`* structure can be viewed.<br>

     - Next, *You* want to be able to visually traverse the whole (if desired) structure and view the mapped `BST level-based output`.<br>
     - The purpose, or idea is to better visuallize how the traversal functions using a data source.<br>   








---

### `Red-Black Tree`

A `Red-Black Tree Search` algorithm is a `self-balancing` binary search tree. It ensures balance by maintaining certain properties:<br>

1. Each `node` is either `*red*` or `*black*`.<br>
2. The `root` is always `*black*`.<br>
3. No two consecutive `red nodes` exist (a red node cannot have a red child).<br>
4. Every path from a `node` to its descendant `null` `pointers` has the same number of `black nodes`.<br>
5. The longest path from the `root` to a `leaf` is no more than twice the shortest path.<br>

These rules ensure the tree remains approximately balanced, allowing operations like insertion, deletion, and search to run in O(log n) time.<br>

#### How does the `Red-Black Tree Search` function?

The search operation in a Red-Black Tree is similar to searching in a regular binary search tree:<br>

1. Start at the `root`: Begin the search at the `root` `node` of the tree.<br>
2. `Compare`: Compare the `target value` with the `current node's value`.
3. Navigate:<br>
    - If the `target value` is `equal to` the `current node's value`, the search is successful, and the node is found.<br> 
    - If the `target value` is `less than` the `current node's value`, move to the `left child`.<br> 
    - If the target value is greater than the current node's value, move to the right child.<br> 

#### Basic Python Example

Define the `Red-Black Tree Search` Node class.<br> 
```
class Node:
    def __init__(self, value, color):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
```

<br>

```
def search(root, value):
    if root is None:
        return None

    if value == root.value:
        return root
    elif value < root.value:
        return search(root.left, value)
    else:
        return search(root.right, value)
```


#### `red_black_tree.py`output

Now for my next trick! lol... Let's describe the red-black tree search output. Honestly, with more time I would find a way to visually describe this tree differently. I would like to have the output data represented in a hierarchical structure.<br>

- A `Red-Black Tree` is a *balanced* `Binary Search Tree` with *additional rules* for maintaining balance during insertion and deletion.<br>

#### Level 1: The Lexicographically `root`

Starting at the root level. In a Red-Black Tree our entry point into the tree is *`Turtwig`*.<br>
`Turtwig` becomes the `root` of the `Red-Black Tree`. A *Red-Black Tree* maintains the properties of a `Binary Search Tree (BST)`, where each node is ordered based on *lexicographical* comparison of keys.<br>

...*Pump the breaks*... <br>
Why is `Turtwig` the `Root` node of this `Red-Black Tree`? <br>
Recall the `array_Pokemon_input.txt` test file... `Turtwig` is indexed around the `2oth` location on the list...<br>
Looking at the test file, I thought `Pikachu` would be the `root` of the tree...<br>

The `root` of the tree `is not` determined by the position of a node in the input list (like `Pikachu` being first). It depends on the `binary search tree (BST)` *properties* and the *comparison logic* during `insertion`.<br>

How the `root` is determined:<br>

- 1. When `nodes` are `inserted` into a `binary search tree`, the `keys` are compared to determine their placement: <br>
    - Keys that are *smaller* (lexicographically) go to the `left`.<br>
    - Keys that are *larger* go to the `right`.<br>
    - In this case, the comparison is based on the *full string* representation of each nodes data:<br>
        - Data being: Pokémon's name, Pokémon's Character Type(Electric, Water...), and the color_list data.<br>

`Turtwig`: (Grass, 🟩 = Grass Green) is *lexicographically* `smaller` than `Pikachu`: (Electric, 🟨 = Bright Yellow)<br> 
is it thought?<br>

Consider this where: `"A" < "B", "a" < "b"`.<br>

- *Side Note* If the first character of *two strings* are the same, then the next characters are compared:<br>

`Turtwig (Grass, 🟩 = Grass Green)` is *smaller than* `Pikachu (Electric, 🟨 = Bright Yellow)`, because `"T" < "P"` (the first characters).<br>

...*Hmmm*... Wait! Why, or how would  "T" be less than "P"...<br>
But if you view the Wiki for the List of `Unicode Characters`, you see that `"P"` is valued at `80`, and "T" at `84`...<br>
```
Code   ->	Glyph	Decimal	Octal	Description	           #
U+0050 ->    P	     80	    0120	Latin Capital letter P	0049
U+0054 ->    T	     84	    0124	Latin Capital letter T	0053
```
This is because we are comparing the *whole* `string` of data, not just the Pokémon character names.<br>

This is how I am thinking of it:<br>
*lexicographically* where `smaller` than the proceeding alphabetical character...<br>
```
Turtwig vs Pikachu
0000001    1111110

```
In the above section, I think that Turtwig is less than Pikachu because the letters in Pikachu's name: `Pikach` have a Unicode value *less than* the letters in Turtwig's name: `Turtwi`. So, to me, Pikachu receives a value indicator of `"1"`. Meaning Turtwig has less positive values. <br>

...Ok!...<br>

The code compares the *whole* string of combined data, including the parentheses, comma, equals symbols, etc.: <br>

```
Pikachu (  Electric  , 🟨 = Bright Yellow)
1111110 == 11010111  1
Turtwig (  Grass, 🟩 = Grass Green)
0000001 == 001010
```
I am not too sure if I would or should line up the character equally to visually show the *lexicographically* depiction...<br> 
(*TODO*: finish this display. Should the characters line up or not?)<br>

...Anyways... The Pikachu `string-data` receives more positive values than Turtwig, making Turtwig the root of this red_black_tree.py list. <br>

#### Level 2

- **Snorlax (Normal, ⬜ = Gray) (red)**
- **Zoroark (Dark, ⬛ = Dark Gray) (red)**

#### Level 3

- **Rayquaza (Dragon, 🟦 = Blue) (black)**
- **Togepi (Fairy, 🟪 = Pink) (black)**
- **Zekrom (Electric, 🟨 = Bright Yellow) (black)**

...Continued levels...<br>

#### Levels 12 & 13

- **Level 12**: `Chespin (Grass, 🟩 = Grass Green) (black)`
- **Level 13**: `Corviknight (Flying, 🟦 = Sky Blue) (red)`

*Levels* `1` to `13` show a `balanced` structure, where `nodes` *alternate* between `red` and `black`. The `balancing` ensures that no *path* from the `root` to a `leaf` is more than twice as long as any other *path*.<br>

```
Enter a command: display

Red-Black Tree Structure:
`- Turtwig (Grass, 🟩 = Grass Green) (black)
   |- Snorlax (Normal, ⬜ = Gray) (red)
   |  |- Rayquaza (Dragon, 🟦 = Blue) (black)
   |  |  |- Pikachu (Electric, 🟨 = Bright Yellow) (red)
   |  |  |  |- Mewtwo (Psychic, 🟧 = Light Red) (black)
   |  |  |  |  |- Lugia (Psychic, 🟧 = Light Red) (red)
   |  |  |  |  |  |- Eevee (Normal, ⬜ = Gray) (black)
   |  |  |  |  |  |  |- Charmander (Fire, 🟧 = Fire Orange) (black)
   |  |  |  |  |  |  |  |- Bulbasaur (Grass, 🟩 = Grass Green) (black)
   |  |  |  |  |  |  |  |  |- Ampharos (Electric, 🟨 = Bright Yellow) (black)
   |  |  |  |  |  |  |  |  `- Butterfree (Bug, 🟩 = Light Green) (black)
   |  |  |  |  |  |  |  |     `- Celebi (Grass, 🟩 = Grass Green) (red)
   |  |  |  |  |  |  |  `- Dialga (Dragon, 🟦 = Blue) (red)
   |  |  |  |  |  |  |     |- Deoxys (Psychic, 🟧 = Light Red) (black)
   |  |  |  |  |  |  |     |  |- Cyndaquil (Fire, 🟧 = Fire Orange) (red)
   |  |  |  |  |  |  |     |  |  |- Chespin (Grass, 🟩 = Grass Green) (black)
   |  |  |  |  |  |  |     |  |  |  `- Corviknight (Flying, 🟦 = Sky Blue) (red)
   |  |  |  |  |  |  |     `- Diancie (Fairy, 🟪 = Pink) (red)
   |  |  |  |  |  |  `- Greninja (Water, 🟦 = Aqua Blue) (black)
   |  |  |  |  |  |     |- Gengar (Ghost, 🟦 = Dark Blue) (red)
   |  |  |  |  |  |     |  |- Gardevoir (Psychic, 🟧 = Light Red) (black)
   |  |  |  |  |  |     |  `- Giratina (Ghost, 🟦 = Dark Blue) (black)
   |  |  |  |  |  |     `- Lucario (Fighting, 🟥 = Fire Truck Red) (red)
   |  |  |  |  |  |        |- Keldeo (Water, 🟦 = Aqua Blue) (black)
   |  |  |  |  |  |        |  |- Grookey (Grass, 🟩 = Grass Green) (red)
   |  |  |  |  |  |        |  `- Koraidon (Dragon, 🟦 = Blue) (red)
   |  |  |  |  |  `- Metagross (Steel, 🔳 = Steel Blue) (black)
   |  |  |  |  |     |- Lycanroc (Rock, 🟫 = Light Brown) (black)
   |  |  |  |  |     |  |- Lunala (Ghost, 🟦 = Dark Blue) (red)
   |  |  |  |  |     |  `- Marshadow (Ghost, 🟦 = Dark Blue) (red)
   |  |  |  |  `- Pidgeot (Flying, 🟦 = Sky Blue) (red)
   |  |  |  |     |- Palkia (Dragon, 🟦 = Blue) (black)
   |  |  |  |     |  |- Miraidon (Dragon, 🟦 = Blue) (red)
   |  |  |  |     |  `- Pawmi (Electric, 🟨 = Bright Yellow) (red)
   |  |  `- Snivy (Grass, 🟩 = Grass Green) (red)
   |  |     |- Reshiram (Fire, 🟧 = Fire Orange) (black)
   |  |     |  `- Rowlet (Grass, 🟩 = Grass Green) (red)
   |  `- Togepi (Fairy, 🟪 = Pink) (black)
   |     |- Squirtle (Water, 🟦 = Aqua Blue) (red)
   |     |  |- Solgaleo (Steel, 🔳 = Steel Blue) (black)
   |     |  |  `- Sprigatito (Grass, 🟩 = Grass Green) (red)
   |     `- Treecko (Grass, 🟩 = Grass Green) (black)
   `- Zoroark (Dark, ⬛ = Dark Gray) (red)
   |     |- Squirtle (Water, 🟦 = Aqua Blue) (red)
   |     |  |- Solgaleo (Steel, 🔳 = Steel Blue) (black)
   |     |  |  `- Sprigatito (Grass, 🟩 = Grass Green) (red)
   |     `- Treecko (Grass, 🟩 = Grass Green) (black)
   `- Zoroark (Dark, ⬛ = Dark Gray) (red)
   |     `- Treecko (Grass, 🟩 = Grass Green) (black)
   `- Zoroark (Dark, ⬛ = Dark Gray) (red)
   `- Zoroark (Dark, ⬛ = Dark Gray) (red)
      |- Zekrom (Electric, 🟨 = Bright Yellow) (black)
      |  |- Yveltal (Dark, ⬛ = Dark Gray) (red)
      |  |  |- Xerneas (Fairy, 🟪 = Pink) (black)
      |  |  `- Zamazenta (Steel, 🔳 = Steel Blue) (black)
      |  |     |- Zacian (Steel, 🔳 = Steel Blue) (red)
      |  |     `- Zarude (Dark, ⬛ = Dark Gray) (red)
```


---

#### `Red-Black Tree Search` *BEST* Method use:

  - Efficient at looking up dynamic datasets.<br>
  - Situations requiring frequent insertions and deletions while preserving order.<br>

- **Big`O` Runtime:**  
  - Insert, Delete, Search: O(log n).  

- **Use Cases:**  
  - Maintaining a balanced tree structure dynamically.
  - Ensures that the height of the tree remains logarithmic, avoiding performance degradation.
  - Ideal for implementing ordered maps, sets, or associative containers.

---

## Noted Sources

- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)  
- [Python Collections](https://docs.python.org/3/library/collections.html#collections.deque)
- [Python Root Nodes](https://docs.python.org/3/library/ast.html#root-nodes)
- [Binary Tree Library](https://binarytree.readthedocs.io/en/main/index.html#)
- [Matplotlib](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot)  
- [Unicode Value List](https://en.wikipedia.org/wiki/List_of_Unicode_characters)


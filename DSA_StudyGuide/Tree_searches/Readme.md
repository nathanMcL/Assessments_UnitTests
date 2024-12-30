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

Located in this sub-directory:  <br>
`DSA_StudyGuide\DSA_Text_files\see_test_files.txt`  <br>

Using the Python scripts: <br>

- Main: `Tree_Searches.py`<br>
- Depth-First Search (DFS): `dfs.py`<br>
- Breadth-First Search (BFS): `bfs.py` <br>
- Tree: `tree.py` <br>
- Binary Tree: ` ` <br>
- Binary Search Tree: ` ` <br>
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






### `Binary Tree`

What is?

- **Big`O` Runtime:**  
  - Insert, Delete, Search: O(n) (unbalanced), O(log n) (balanced).  

- **Use Cases:**  
  - Representing arithmetic expressions.
  - Organizing hierarchical data with strict binary conditions.

---

### `Binary Search Tree (BST)`

- **Big`O` Runtime:**  
  - Insert, Delete, Search: O(log n) (average), O(n) (worst case, unbalanced).  

- **Use Cases:**  
  - Efficient searching and sorting.
  - Dynamic sets and dictionaries.

---

### `Red-Black Tree`

- **Big`O` Runtime:**  
  - Insert, Delete, Search: O(log n).  

- **Use Cases:**  
  - Maintaining a balanced tree structure dynamically.
  - Storing ordered data while ensuring balance.

---

## Noted Sources

- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)  
- [Python Collections](https://docs.python.org/3/library/collections.html#collections.deque)  

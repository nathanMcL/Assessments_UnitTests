# Data Structures and Algorithms Study Guide

## Tree Search Algorithms:

- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Tree
- Binary Tree
- Binary Search Tree
- Red-Black Tree

---

## Set Up

Using these test files:  
`Emoji_description.txt`  
`array_Emoji_input.txt`  

Located in this sub-directory:  
`DSA_StudyGuide\DSA_Test_files\see_test_files.txt`  

Using the Python script:  
`Tree_Searches.py`  

---

### `Depth-First Search (DFS)`

DFS algorithm explores a graph by starting at a chosen `node` and traversing as far down `one branch` as possible before backtracking to explore other branches, essentially *"diving deep"* into the graph until it reaches a dead end before moving on to other potential paths. <br>
The `DFS` uses a `stack` data structure to keep track of visited `nodes` and the path to backtrack to; this process continues until all reachable `nodes` in the graph have been visited.<br>

- **Big`O` Runtime:**  
  - Time Complexity: O(V + E) where V is vertices and E is edges (for graphs).  
  - Space Complexity: O(H) where H is the height of the tree.  

- **Use Cases:**  
  - Solving puzzles like mazes or pathfinding.
  - Evaluating expressions in expression trees.

---

### `Breadth-First Search (BFS)`

The *`Breadth-First Search`* (BFS) algorithm explores a `graph` or `tree` by systematically visiting all `nodes` at the current depth level before moving on to the next level, essentially "rippling out" from a starting node, ensuring it finds the shortest path to any target node by checking all nodes one "hop" away before moving to nodes further away; it uses a `queue` data structure to keep track of nodes to visit, adding neighbors of the currently visited node to the queue as they are discovered.

- **Big`O` Runtime:**  
  - Time Complexity: O(V + E) for graphs.
  - Space Complexity: O(W) where W is the maximum width of the tree.  

- **Use Cases:**  
  - Finding the shortest path in unweighted graphs.
  - Peer-to-peer networking.

---

### `Tree`

- **Big`O` Runtime:**  
  - Insert, Delete, Search: O(n) (worst case, unbalanced tree).  

- **Use Cases:**  
  - Representing hierarchical data such as organizational charts or file systems.

---

### `Binary Tree`

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

# Data Structures and Algorithms Study Guide

## Heap

---

## Set Up

Using these test files: <br> 
`array_Pokemon_input.txt`<br>
`pokemon_winPercentages.txt`<br>

Located in this sub-directory:  <br>
`DSA_StudyGuide\DSA_Text_files\see_test_files.txt`  <br>

Using the Python scripts: <br>
`heap.py`: Main program file. <br> 
`heap_min.py`: Minimum Heap Method<br> 
`heap_max.py`: Maximum Heap Method<br>


---

## The Plan...

1. Using the test files we want to `read the file`.<br>
2. Next we want to build/create/implement (What is a better descriptive word?) the `heap` (heap_code) from the `array_Pokemon_input.txt` file list of Pokémon character names and `sort` them alphabetically (They could be sorted other ways: lexicographically, length...)<br>
3. After '`sorting`' *`combine`* that array Pokémon list with the `pokemon_winPercentages.txt` file's fake/arbitrary win percentages.<br> 

```
17.8%
2.1%
29.5%
.
.
.
32.9%

```

4. Lastly, we want to conduct the `minimum` and `maximum` `heap` function by using the percentages to organize the data. <br>


---

### What is a Heap?

That is a heap of waste... Have you ever seen a heap of data.?.<br>
The way I am thinking of a `heap` is that the algorithm is meant to process or sort through large data sets...<br>

*Heaps* are a specialized binary tree data structure of items organized with a specific structure and rules.<br>

1. Mimimum Heap: The *value* of each `parent node` is *less than* or *equal to* the *values* of its `children`. The smallest *value* is always the `root` (heap[0]).<br>

2. Maximum Heap: The *value* of each `parent node` is *greater than* or *equal to* the `values` of its `children`. The largest `value` is always the `root`.<br>

### Structure of a `Heap`

Heaps are `binary trees` with two *key* characteristics:<br>

1. Complete Binary Tree:<br>

  - All the levels are fully filled except "possibly" the last, which is filled from *left* to *right*.<br>

2. Heap Propety:

  - The `parent-child` relationships maintain the `min-heap` or `max-heap` "rules".

`Heaps` use `arrays` to effciently manage their structure.<br>

...Consider...<br>
An array k = `[5, 7, 3, 11, 8, 9, 2]`<br>
Sort min-heap k = `[2, 7, 3, 11, 8, 9, 5]`<br>

Visual: <br>

```
      2
    /   \
   7     3
  / \   / \
 11  8 9   5

```

- Parent: The `parent` of the `node` at index `k` is at index `(k-1)//2`.<br>

- Left Child: The `left child` of the `node` at index `k` is at index `2*k + 1`.<br>

- Right Child: The `right child` of the `node` at index `k` is at index `2*k + 2`.<br>

... But why is `"7"` the `left-child` of the `root`? Shouldn't `"3"` and `"5"` be the `left` and `right` children.?.<br>

...Ok...<br>

The smallest number in the array is `"2"`, *two* is the `root`.<br>
The `array's` *second* and *third* smallest elements, `"7"` and `"3"`, become the `left` and `right children`.

The reason why `"7"` is the `left-child` of the parent `root` and not `"3"` and `"5"` is because although it states `"every parent node is smaller than or equal to its children"`.<br>
The heap does not have to be fully sorted, it ensures that the `smallest` element is always the `root` `(heap[0])`.<br>

1. Step 1: Insert `"5"`.<br>
The `array` starts with `"5"` as the root of the list.<br>

```
     Root
      5
```

2. Step 2: Insert `"7"`.<br>
Seven becomes the `left-child` of `"5"`.<br>

```
     Root
      5
    /
   7
```

3. Step 3: Insert `"3"`.<br>
Three now becomes the `root` since `3 < 5`.<br>
`"5"` becomes the `right-child` of three.<br>

```
     Root
      3
    /   \
Left_C  Right_C    
   7      5
```

4. Step 4: Insert `"11"`.<br>
Eleven becomes the `left-child` of `"7"`, since `11 > 7`

```
     Root
      3
    /   \
Left_C  Right_C    
   7      5
  /      
 11  
```

5. Step 5: Insert `"8"`.<br>
Because `"8"` is `greater than` `"7"` it becomes the `right-child` of `"7"`.<br>

```
     Root
      3
    /   \
Left_C  Right_C    
   7      5
  / \    
 11  8 
```

6. Step 6: Insert `"9"`.<br>
Nine becomes the `left-child` of `"5"`, since `9 > 5`.<br>

```
     Root
      3
    /   \
Left_C  Right_C    
   7      5
  / \    /  
 11  8  9
```

7. Step 7: Insert `"2"`.<br>
Recall `"2"` is the last element in the unsorted array: `[5, 7, 3, 11, 8, 9, 2]`<br>
Two is also the smallest number. Since `2 < 3`, we swap `2` with `3`. Then, making `3` the `right-child` of two, moving `5` to the last `node` position.<br> 

```
     Root
      2
    /   \
Left_C  Right_C    
   7      3
  / \    / \ 
 11  8  9   5
```

So, back to my previous thought. To completly `"sort"` the `heap` (minimum or maximum) you would need to continue the process of extracting the elements until the list is sorted (`heap sort`).<br>


### Minimum Heap: `heap_min.py`

#### Step 1:

Simulate the Minimum Heap Algorithm<br>
Loaded Pokémon Data:<br>

```
 Pikachu
 Charmander
 Bulbasaur
 Squirtle
 Eevee
.
.
.
Koraidon
Miraidon
```

Loaded Win Percentages:<br>

```
 17.8%
 2.1%
 29.5%
 11.4%
 5.7%
 22.9%
 31.2%
 16.3%
.
.
.
3.1%
32.9%
```

### Step 2:

Combined Pokémon with Win Percentages:<br>
```
 Pikachu - 17.8%
 Charmander - 2.1%
 Bulbasaur - 29.5%
 Squirtle - 11.4%
 Eevee - 5.7%
 Butterfree - 22.9%
.
.
.
Koraidon - 3.1%
Miraidon - 32.9%
```

### Step 3:

Building Min-Heap...<br>

Min-Heap Built:<br>
```
 Ampharos - 27.1%
 Charmander - 2.1%
 Bulbasaur - 29.5%
 Deoxys - 24.3%
 Corviknight - 4.2%
 Butterfree - 22.9%
.
.
.
Palkia - 4.9%
Miraidon - 32.9% 
```

### Step 5:

Extracted Minimum Root Element:<br> 
`Ampharos - 27.1%`<br>

Heap after extraction:<br>
```
 Bulbasaur - 29.5%
 Charmander - 2.1%
 Butterfree - 22.9%
 Deoxys - 24.3%
 Corviknight - 4.2%
 Giratina - 26.8%
.
.
.
Pawmi - 16.7%
Palkia - 4.9%
```

### Step 6: `Add`

`Add` an element to the heap.<br>
Adding an `element` (or more data) puts the added element at the *Root* of the Step 2: `Combined Pokémon with Win Percentages:`<br>

Enter a command: `add Absol - 7.3%`<br>

```
Element 'Absol - 7.3%' added to the heap:
 Absol - 7.3%
 Charmander - 2.1%
 Bulbasaur - 29.5%
 Deoxys - 24.3%
 Corviknight - 4.2%
.
.
.
 Palkia - 4.9%
 Miraidon - 32.9%
```

### Step 7: `Peek`

What does *"Peek"* do?<br>

  - The `peek` command is used to *view* the smallest (root) element `without` removing it.<br>

Enter a command: `peek`<br>

```
Step 4: Peek Minimum Root Element: Absol - 7.3%
```

### Step 8: `Extract`

  - The `extract` command is used to *extract* the smallest element from the heap.<br>
 
```
Step 5: Extracted Minimum Root Element: Absol - 7.3%

Heap after extraction:
 Bulbasaur - 29.5%
 Charmander - 2.1%
 Butterfree - 22.9%
 Deoxys - 24.3%
.
.
.
 Pawmi - 16.7%
 Palkia - 4.9%
```

### Step 8: `n_smallest` 
 
 - With `n_smallest` we want to extract `n` values (test files only have 48 elements).<br>

``` 
Enter a command: n_smallest 5

5 Smallest elements in the heap:
 Bulbasaur - 29.5%
 Butterfree - 22.9%
 Celebi - 6.5%
 Charmander - 2.1%
 Chespin - 28.4%
```

---

### Maximum Heap: `heap_max.py`

#### Maximum Heap Step 1:

Simulate the Maximum Heap Algorithm<br>



































---

### Heap Big`O`

- **Big`O` Runtime**:  
  - **Access (Peek)**: `O(1)`  
  - **Insertion**: `O(log n)`  
  - **Deletion**: `O(log n)`  

- **Use Cases**:  
  - Implementing priority queues.  
  - Finding the smallest or largest element efficiently (min-heap or max-heap).  
  - Scheduling tasks where priority determines execution order.  
























---

## Noted Sources

- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)  
- [Python Collections](https://docs.python.org/3/library/collections.html#collections.deque)
- [Heap, Priority Que](https://docs.python.org/3/library/heapq.html)

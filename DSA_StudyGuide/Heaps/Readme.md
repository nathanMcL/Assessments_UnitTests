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

1. Using the test files we want to load and `read the file`.<br>
2. Next, we want to *`Combine`* the `heap` data: `array_Pokemon_input.txt` & `pokemon_winPercentages.txt` files.<br>
3. `Build` the Minimum Heap.<br>
4. `Extract` the minimum `root element`.
5. `Sort`: `sort` them alphabetically (They could be sorted other ways: lexicographically, length...)<br> 

    - (*TODO*) Have to redo the sort function. Once the heap is formed (`Alphabetical`, `Numerical`) *HOW* do we want to sort? Numerically, Alphabetically.?. What sort method would best be able to visually disribe the minimum heap?<br>  


```
17.8%
2.1%
29.5%
.
.
.
32.9%

```

4. Lastly, we want to conduct the `minimum` and `maximum` `heap` function to visually describe how the two methods function with the data. <br>


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
Two is also the smallest number. Since `2 < 3`, we swap `2` with `3`. Then, making `3` the `right-child` of two, moving `5` to the last `node` posisiton.<br> 

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

---

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
Rayquaza - 1.5%
Rowlet - 1.9%
Keldeo - 2.7%
Charmander - 2.1%
Corviknight - 4.2%
Koraidon - 3.1%
.
.
.
Butterfree - 22.9%
Miraidon - 32.9% 
```

### Step 5:

Extracted Minimum Root Element:<br> 
`1.5, Rayquaza - 1.5%`<br>

Heap after extraction:<br>
```
 1.9, Rowlet - 1.9%
 2.1, Charmander - 2.1%
 2.7, Keldeo - 2.7%
 5.2, Xerneas - 5.2%
 4.2, Corviknight - 4.2%
 3.1, Koraidon - 3.1%
.
.
.
18.5, Dialga - 18.5%
22.9, Butterfree - 22.9%
```

### Step 6: `Add`

`Add` an element to the heap.<br>
Adding an `element` (or more data) puts the added element at the *Root* of the Step 2: `Combined Pokémon with Win Percentages:`<br>

Enter a command: `add Absol - 7.3%`<br>

```
Element 'Absol - 7.3%' added to the heap:
Rowlet - 1.9%
Charmander - 2.1%
Keldeo - 2.7%
Xerneas - 5.2%
Corviknight - 4.2%
.
.
.
Butterfree - 22.9%
Absol - 7.3%
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
Step 5: Extracted Minimum Root Element: 1.9, Rowlet - 1.9%

Heap after extraction:
2.1, Charmander - 2.1%
4.2, Corviknight - 4.2%
2.7, Keldeo - 2.7%
5.2, Xerneas - 5.2%
5.7, Eevee - 5.7%
.
.
.
Pawmi - 16.7%
Palkia - 4.9%
```

### Step 9: `n_smallest` 
 
 - With `n_smallest` we want to extract `n` values (test files only have 48 elements).<br>

``` 
Enter a command: n_smallest 5

5 Largest elements in the heap:
2.1, Charmander - 2.1%
2.7, Keldeo - 2.7%
3.1, Koraidon - 3.1%
3.8, Togepi - 3.8%
4.2, Corviknight - 4.2%
```

---

### Maximum Heap: `heap_max.py`

#### Maximum Heap Step 1:

Similarly to the `minimum heap`, the `maximum heap` instead the *maximum heap* focuses on the elements within the combined (in this case) lists.<br>

...Skipping steps 1 & 2...<br>

#### Convert the Data for the `Maximum Heap` to *tuples*

...So...<br>
When we conduct a `minimum heap` function (the *smallest* number at the top) in Python, the `heap` naturally creates a `Mini-Heap`.<br>
To Create the `Maximum-Heap` we have to *flip* it into a `Max-Heap`. That means we have to make the numbers `negative`, so the *largest* value appears at the top.<br>

Helper function to *flip* percentages to `negative` number `tuples` (to store *both* the sorting value and original data) for the heap operation.<br>

`Min-Heap Built`:     ---  `Max-Heap Built`:<br>
```
Rayquaza - 1.5%             Miraidon - 32.9%
Rowlet - 1.9%               Treecko - 32.4%
Keldeo - 2.7%               Pidgeot - 31.2%
Charmander - 2.1%           Yveltal - 31.9%
Corviknight - 4.2%          Lucario - 30.8%
Koraidon - 3.1%             Bulbasaur - 29.5%
.                           .
.                           .
.                           .
Butterfree - 22.9%          Koraidon - 3.1%
Miraidon - 32.9%            Togepi - 3.8%
                      ---
```

```
def ctn_tuples(data):
    converted = [(-float(item.split(' - ')[1].strip('%')), item) for item in data]
    return converted
```

- This function "preps" the data for the `max-heap`.<br>
- It takes the `Pokémone` data like "`Pikachu - 17.8%`" and turns the percentage into a `negative` number.<br>

#### Build the `Maximum Heap`

- This function `organizes` the Pokémon data into a Max-Heap.<br>
- It first `converts` the data (using the previous function) and then rearranges it with `heapq.heapify()` to follow the heap rules.<br>
- The `return` *builds* it and `prints` out the new `heap`. <br>

```
def build_max_heap(data):
    print("\nStep 3: Building Max-Heap...")
    max_heap = ctn_tuples(data)
    heapq.heapify(max_heap)
    print(f"\nMax-Heap Built:")
    for _, item in max_heap:
        print(f" {item}")
    return max_heap
```

...Output...<br>

```
Step 3: Building Max-Heap...

Max-Heap Built:
 Miraidon - 32.9%
 Treecko - 32.4%
 Pidgeot - 31.2%
 Yveltal - 31.9%
 Lucario - 30.8%
```

Step 5: `Extracted Maximum Root Element`: `Miraidon - 32.9%`<br>

```
def extract_max(heap):
    if not heap:
        print("Error: No heap to extract from.")
        return None
    max_element = heapq.heappop(heap)[1] # Heap Pop
    print(f"\nStep 5: Extracted Maximum Root Element: {max_element}")
    print(f"\nHeap after extraction:")
    for _, item in heap:
        print(f" {item}")
    return max_element
```

...Output...<br>

Notice in this section that the Heap *elements* are not in order...<br>
That is because in the *Minimum Heap* `heap_min` we have the code such that it orders the *heap* in numerical order.<br>

In *Maximum Heap* `heap_max` the code *is NOT* in numerical order, therfore the `extraction` is *extracting*  the *Maximum Element*.<br>    

```
Heap after extraction:
 Treecko - 32.4%
 Yveltal - 31.9%
 Pidgeot - 31.2%
 Deoxys - 24.3%
 Lucario - 30.8%
.
.
.
Corviknight - 4.2%
Turtwig - 7.6%
Cyndaquil - 13.0%
Zarude - 9.8%
Eevee - 5.7%
Pawmi - 16.7%
Koraidon - 3.1%
```

#### Adding data to the heap

- This function lets you `add` a new `Pokemon` with its win percentage into the heap.<br>
- Recall, with  the `Max-Heap` the percentage is *flipped*, turned `negative` so the heap stays a `Max-Heap`.<br>
- The `heap` is then *automatically* rearranged to keep the strongest `Pokémon` on top.<br>

`Command`: `add Garchomp - 35.5%` <br>

```
def add_to_heap(heap, item):
    heapq.heappush(heap, (-float(item.split(' - ')[1].strip('%')), item))
    print(f"\nElement '{item}' added to the heap:")
    for _, h in heap:
        print(f" {h}")
```

#### Let's `peek` at our *Strongest* `Pokemon`

- In this function we can check which Pokemon has the highest win percentages *without* removing it.<br>
- We are simply '`printing`' the *element* at the top of the `heap`.<br>

`Command`: `peek`<br>

```
def peek_max(heap):
    if heap:
        print(f"\nStep 4: Peek Maximum Root Element: {heap[0][1]}")
    else:
        print("Error: Heap is empty.")
```

#### `Removing` the *Strongest* Pokemon

- In this function we want to `remove` and `show` the Pokemon with the `highest` *win percentage*.<br>
- The `heap` is *reshuffled* after `removal` to keep the next strongest *Pokemon* at the top.<br>

`Command`: `extract`<br>

`Before`: *Garchomp* is at the `top`.<br>
`After`: *Garchomp* is `removed`, and the *next* `strongest` Pokemon takes its place.<br>

```
def extract_max(heap):
    if not heap:
        print("Error: No heap to extract from.")
        return None
    max_element = heapq.heappop(heap)[1]
    print(f"\nStep 5: Extracted Maximum Root Element: {max_element}")
    print(f"\nHeap after extraction:")
    for _, item in heap:
        print(f" {item}")
    return max_element
```

#### Finding the `Top` *Pokemon*

- This function lets you see the `top` *N* of Pokemon without changing the heap.<br>
- It uses `heapq.nlargest()` to quickly find the *strongest* Pokemon.<br>

`Command`: `n_largest 3`<br>

```
def n_largest(heap, n):
    largest = heapq.nlargest(n, heap)
    print(f"\n{n} Largest elements in the heap:")
    for _, item in largest:
        print(f" {item}")
```





































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

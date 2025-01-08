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
`heap.py`: Main program file. 
`heap_min.py`: Minimum Heap Method
`heap_max.py`: Maximum Heap Method


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

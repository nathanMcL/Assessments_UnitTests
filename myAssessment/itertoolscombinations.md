## Itertools & Combinations

`https://www.hackerrank.com/challenges/itertools-combinations/problem` <br>

This tool returns the `r` length subsequences of elements from the input iterable. <br>

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order. <br>

## Sample Code

```
>>> from itertools import combinations
>>> 
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
>>> 
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]
```

## Task

- You are given a string `S`. <br>
- Your task is to print all possible combinations, up to size `k`, of the string in lexicographic sorted order. <br>

## Input Format

A single line containing the string `S` and integer value `k` separated by a space. <br>

## Constraints

`0 < k ≤ len(S)` <br>
The String contains only UPPERCASE characters. <br>

## Output Format

Print the different combinations of string `S` on separate lines. <br>


## Sample Input

```
HACK 2
```

## Sample Output

```
A
C
H
K
AC
AH
AK
CH
CK
HK
```













## Noted Sources

- https://docs.python.org/2/library/itertools.html#itertools.combinations
- https://docs.python.org/3/library/itertools.html 

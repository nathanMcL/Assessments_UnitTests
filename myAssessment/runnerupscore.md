## Find the Runner Up Score

`https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem` <br>

Given the participants' score sheet for your University Sports Day, Go Goey Ducks!!! you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up. <br>

## Input Format

The first line contains `n`. The second line contains an array `A[...]` of `n` integers each separated by a space. <br>

## Constraints

- `2 ≤ n ≤ 10` <br>
- `-100 ≤ A[i] ≤ 100` <br>

## Output Format

Print the runner-up score.<br>

Sample Input `O` <br>

```
5
2 3 6 6 5
```

## Sample Output `O`

```
5
```

## Explanation `O`

Given list is `[2, 3, 6, 6, 5]`. The maximum score is `6`, second maximum is `5`. Hence, we print `5` as the runner-up score. <br>

I first attempted the discussion solution I found, it worked but... <br> 

## `max()` Filtering

Instead of sorting which isn't necessary for this task. This method identifies the maximum score, removes all the instances of the max score, and then finds the runner-up (new maximum). <br> 

- 1. Find the Maximum Score: Use `max(arr)` to identify the highest score.  <br>
- 2. Remove instances of Maximum Scores and createa `new` list:
`arr = [score for score in arr if score != max_score]`. <br>
- 3. Find Runner-up: Use `max(arr)` again on the `new` list to find the runner-up. <br>

```

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_score = max(arr) # Find the maxium score
    arr = [score for score in arr if score != max_score] # Remove all the instances of max_score
    runner_up_score = max(arr) # Find the new maximum
    print(runner_up_score) # Print the runner-up score 

```

... Or... <br>

## Use a `Priority Queue`

- Use Python's `heapq` module to extract the two largest unique values quickly. <br>

- 1. Remove the Duplicates: Covert the input list to a set to eliminate the duplicate values:

`arr = list(set(map(int, input().split())))` <br>

- 2. Find the `2` largest values: Use `heapq.nlargest()` to get the two largest `unique` values as a list. <br>

- 3. `Print` the second element on the list. <br>

Focuses on the `2` top largest numbers. <br>
Better for larger datasets (although this problem has constraints). <br>

```
import heapq

if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))  # Remove duplicates
    largest_two = heapq.nlargest(2, arr)  # Get the two largest unique values
    print(largest_two[1])  # The second largest is the runner-up
```
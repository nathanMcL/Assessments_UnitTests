
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_score = max(arr) # Find the maxium score
    arr = [score for score in arr if score != max_score] # Remove all the instances of max_score
    runner_up_score = max(arr) # Find the new maximum
    print(runner_up_score) # Print the runner-up score 

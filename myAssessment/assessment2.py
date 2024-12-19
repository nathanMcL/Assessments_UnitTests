# within the a company gaming distrbuiton system, a logistic corrdinator is faced with the task of efficiently distribuitng
# a collection of n compter games among k different children.
# Each game is characterized by its size, denoted by gameSize[i] for 1 <= i <= n.
# Eample n = 4
# gameSize[] = [4, 8, 6, 12]
# k = 3

# Complete the 'getMinSize' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY gameSize
#  2. INTEGER k
#
# Constrints:
# 1 <= k <= n <= 2 * 10^5
# 1 <= gameSize[i] <= 10^9
# n <= 2*k

def canDistribute(gameSize, k, maxSize):
    """
    Helper function to check if it's possible to distribute games
    such that no child receives a total size greater than maxSize.
    """
    current_sum = 0
    children_needed = 1  # Start with the first child

    for size in gameSize:
        if current_sum + size > maxSize:
            # Allocate to a new child
            children_needed += 1
            current_sum = size
            if children_needed > k:
                return False
        else:
            current_sum += size
    
    return True

def getMinSize(gameSize, k):
    """
    Function to find the minimum possible maximum size of games
    assigned to any child using binary search.
    """
    # Edge case: If k == n, each child gets one game
    if k == len(gameSize):
        return max(gameSize)

    # Binary search between the largest game size and the total size
    low, high = max(gameSize), sum(gameSize)

    while low < high:
        mid = (low + high) // 2
        if canDistribute(gameSize, k, mid):
            high = mid  # Try for a smaller maxSize
        else:
            low = mid + 1  # Increase the allowed maxSize
    
    return low

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Input parsing
    gameSize_count = int(input().strip())
    gameSize = list(map(int, input().strip().split()))
    k = int(input().strip())

    # Compute result
    result = getMinSize(gameSize, k)

    # Output the result
    fptr.write(str(result) + '\n')
    fptr.close()

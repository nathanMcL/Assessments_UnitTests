# Data analysist at A company are analyzing a data of set n strings in
# the array dataSet, each consisting of lowercase English letters. 
# Each character in a string corresponds to a particular feature.

# Complete the function getMaxInformationGain,
# getMaxInformationGain has the following arguments:
# str dataSet[n]: an array of strings, 
# int max_common_features: the maximum number of common features allowed between two data points
# 
# Returns: 
# int the maximum possible information gain
# 
# Constraints:
# 2 <= n <= 1000
# 1 <=max_common_features <= 1000
# 1 <=len(dataSet[i]) <= 1000

from collections import Counter

def getMaxInformationGain(dataSet, max_common_features):
    # Count the frequency of each character in the dataset
    char_count = Counter(char for data in dataSet for char in data)
    
    # Sort the character counts in descending order
    char_count_list = sorted(char_count.values(), reverse=True)
    
    # Calculate cumulative sums for optimization
    prefix_sum = [0] * (len(char_count_list) + 1)
    for i in range(1, len(char_count_list) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + char_count_list[i - 1]

    max_gain = 0
    
    # Calculate information gain
    for i in range(min(max_common_features, len(char_count_list))):
        sum_i = prefix_sum[i + 1]  # Sum of most common features up to index i
        sum_j = prefix_sum[-1] - prefix_sum[i + 1]  # Remaining sum
        max_gain = max(max_gain, sum_i - sum_j)
    
    return max_gain

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    dataSet_count = int(input().strip())

    dataSet = [input().strip() for _ in range(dataSet_count)]

    max_common_features = int(input().strip())

    result = getMaxInformationGain(dataSet, max_common_features)

    fptr.write(str(result) + '\n')

    fptr.close()
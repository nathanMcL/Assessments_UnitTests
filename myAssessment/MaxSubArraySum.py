#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'maximumSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m
#

def maximumSum(a, m):
    # Write your code here

    # Variables
    max_mod_sum = 0
    current_sum = 0
    prefix_sums = []

    # Update the cumulative sum modulo m
    for value in a:
        current_sum = (current_sum + value) % m

        # Update the maximum modulo sum
        max_mod_sum = max(max_mod_sum, current_sum)

        # Find the smallest prefix sum larger than the current sum (wrap-around cases)
        idx = bisect.bisect_right(prefix_sums, current_sum)
        if idx < len(prefix_sums):
            # Use the wrap-around case to calculate the potenial maximum
            max_mod_sum = max(max_mod_sum, (current_sum - prefix_sums[idx] + m) % m)

        # Insert the current cumulative sum into the sorted list
        bisect.insort(prefix_sums, current_sum)

    return max_mod_sum

# Hardcoded test cases to simulate the HackerRank environment
def test_local_input():
    return [
        # Test case 1:
        [
            "1", # Number of queries
            "5 7", # n (array size) and %m (modulo divisor)
            "3 3 9 9 5" # Array elements
        ],
        # Test case 2:
        [
            "1", # Number of queries
            "3 10", # n (array size) and %m (modulor divisor)
            "1 2 3" # Array elements
        ], 
        # Test Case 3 (edge case)
        [
            "1", # Number of queries
            "2 2", # n (array size) and %m (modulor divisor)
            "1000000000 999999999" # Array elements with large values
        ],
    ]

# Using the Hardcoded test cases to simulate the Hackerrank environment
def simulate_test_cases():
    test_cases = test_local_input()
    results = []

    for idx, test_case in enumerate(test_cases, 1):
        print(f"Running Test Case {idx}...")

        # Simulate the input
        input = iter(test_case).__next__

        # Main
        q = int(input().strip())
        for _ in range(q):
            n, m = map(int, input().split())
            a = list(map(int, input().split()))
            result = maximumSum(a, m)
            results.append(results)
            print(f"Result for Test Case {idx}: {result}")

    return results

if __name__ == '__main__':
    simulate_test_cases()

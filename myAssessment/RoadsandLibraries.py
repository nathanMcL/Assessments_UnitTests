#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here

    # If building a library is cheaper than building a road, then build a library in each city
    if c_lib <= c_road:
        return n * c_lib
    
    # Build an adjacencent list for the graph
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for u, v in cities:
        graph[u].append(v)
        graph[v].append(u)

    # Use a set to keep track of visited cities
    visited = set()
    def bfs(start): # Perform a breadth-first search (BFS) to all cities in a connected component
        queue = deque([start])
        visited.add(start)
        size = 0
        while queue:
            city = queue.popleft()
            size += 1
            for neighbor in graph[city]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return size
    
    # Calculate the minimum cost of building libraries and roads
    total_cost = 0
    for city in range(1, n + 1):
        if city not in visited:
            # For each unvisited city, start a new connected component
            component_size = bfs(city)
            # Cost: 1 library + (component_size - 1) roads
            total_cost += c_lib + (component_size - 1) * c_road
    return total_cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()

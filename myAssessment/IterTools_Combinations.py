from itertools import combinations

def generate_combinations_itertools(S, k):
    S = ''.join(sorted(S)) # Check if the string is sorted lexicographically
    results = []
    for i in range(1, k + 1): # Generate combinations of size 1 to k
        for comb in combinations(S, i):
            results.append(''.join(comb))
    return results
            
# Main function to handle multiple test cases
if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().splitlines() # Read all input as lines
    for line in input_data:
        if line.strip(): # Process the non-empty lines
            S, k = line.split()
            k = int(k)
            results = generate_combinations_itertools(S, k)
            print('\n'.join(results))

# To test this function, there is a test file named: `itertool_input.txt` in the same directory.
# Run the this script with the following command:
# `python3 IterTools_Combinations.py < itertool_input.txt`
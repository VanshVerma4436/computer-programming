''' Find Pairs with Given Sum
Scenario:
You are tasked with matching items from two different catalogs based on a target cost.

Problem Statement:
Write a program to find all pairs of integers in an array that sum to a target value.

Input Format:

The first line contains an integer n.
The second line contains n space-separated integers.
The third line contains the target sum.
Output Format:

Print all pairs of integers.
Example:
Input:

5  
1 2 3 4 5  
5
Output:

1 4  
2 3'''

# Read input
n = int(input())
elements = list(map(int, input().split()))
target_sum = int(input())

# Initialize a set to store elements we've seen so far
seen = set()
pairs = []

# Iterate through each element in the array
for num in elements:
    complement = target_sum - num
    if complement in seen:
        pairs.append((complement, num))
    seen.add(num)

# Print the pairs
for pair in pairs:
    print(f"{pair[0]} {pair[1]}")


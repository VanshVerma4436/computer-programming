'''Find the Largest Sum Subarray
Scenario:
You need to identify the best-performing time periods in sales data.

Problem Statement:
Write a program to find the subarray with the largest sum.

Input Format:

The first line contains an integer n.
The second line contains n space-separated integers.
Output Format:

Print the largest sum.
Example:
Input:

5  
-2 1 -3 4 -1 2 1 -5 4
Output:

6'''

# Read input
n = int(input())
elements = list(map(int, input().split()))

# Initialize variables
max_current = max_global = elements[0]

# Apply Kadane's Algorithm
for i in range(1, n):
    max_current = max(elements[i], max_current + elements[i])
    if max_current > max_global:
        max_global = max_current

# Print the largest sum
print(max_global)


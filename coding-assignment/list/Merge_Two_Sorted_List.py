'''Merge Two Sorted Arrays
Scenario:
You are building a tool to merge user data sorted by creation dates.

Problem Statement:
Write a program to merge two sorted arrays into a single sorted array.

Input Format:

The first line contains an integer n, the size of the first array.
The second line contains n sorted integers.
The third line contains an integer m, the size of the second array.
The fourth line contains m sorted integers.
Output Format:

Print the merged sorted array.
Example:
Input:

4  
1 3 5 7  
3  
2 4 6
Output:

1 2 3 4 5 6 7'''

# Read input
n = int(input())
array1 = list(map(int, input().split()))
m = int(input())
array2 = list(map(int, input().split()))

# Initialize pointers for both arrays
i, j = 0, 0
merged_array = []

# Merge both arrays
while i < n and j < m:
    if array1[i] < array2[j]:
        merged_array.append(array1[i])
        i += 1
    else:
        merged_array.append(array2[j])
        j += 1

# Add remaining elements of array1, if any
while i < n:
    merged_array.append(array1[i])
    i += 1

# Add remaining elements of array2, if any
while j < m:
    merged_array.append(array2[j])
    j += 1

# Print the merged sorted array
print(" ".join(map(str, merged_array)))

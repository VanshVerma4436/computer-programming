'''Find All Subarrays with Zero Sum
Scenario:
You are analyzing financial data and need to identify periods where there was no net profit or loss.

Problem Statement:
Write a program to find all subarrays of an array that have a sum of zero.

Input Format:

The first line contains an integer n.
The second line contains n space-separated integers.
Output Format:

Print the starting and ending indices of all subarrays with zero sum.
Example:
Input:

6  
3 4 -7 1 3 3
Output:

[0, 2]  
[3, 4]'''

# Read input
n = int(input())
elements = list(map(int, input().split()))

# Initialize variables
zero_sum_subarrays = []
sum_to_index = {}
current_sum = 0

# Iterate through the array
for i in range(len(elements)):
    current_sum += elements[i]
    
    if current_sum == 0:
        zero_sum_subarrays.append((0, i))
    
    if current_sum in sum_to_index:
        start_indices = sum_to_index[current_sum]
        for start_index in start_indices:
            zero_sum_subarrays.append((start_index + 1, i))
    
    if current_sum in sum_to_index:
        sum_to_index[current_sum].append(i)
    else:
        sum_to_index[current_sum] = [i]

# Print the results
for subarray in zero_sum_subarrays:
    print(f"[{subarray[0]}, {subarray[1]}]")

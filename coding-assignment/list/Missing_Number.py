'''Find the Missing Number in a Sequence
Scenario:
A data logger is tracking sequential numbers but occasionally misses an entry. Your job is to identify the missing number.

Problem Statement:
Write a program to find the missing number in an array containing n unique integers from 1 to n+1.

Input Format:

The first line contains an integer n.
The second line contains n space-separated integers.
Output Format:

Print the missing number.
Example:
Input:

5  
1 2 4 5 6
Output:

3'''

# Read input
n = int(input())
elements = list(map(int, input().split()))

# Calculate the expected sum of numbers from 1 to n+1
expected_sum = (n + 1) * (n + 2) // 2

# Calculate the actual sum of the given numbers
actual_sum = sum(elements)

# Find the missing number
missing_number = expected_sum - actual_sum

# Print the missing number
print(missing_number)

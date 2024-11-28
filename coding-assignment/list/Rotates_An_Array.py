'''Rotate an Array
Scenario:
You are tasked with implementing a feature for a digital carousel that rotates content based on user input.

Problem Statement:
Write a program to rotate an array k steps to the right.

Input Format:

The first line contains two integers, n (size of the array) and k (number of steps to rotate).
The second line contains n space-separated integers representing the elements of the array.
Output Format:

Print the rotated array.
Example:
Input:

6 2  
1 2 3 4 5 6
Output:

5 6 1 2 3 4'''

# Read input
n, k = map(int, input().split())
elements = list(map(int, input().split()))

# Rotate array
k = k % n  # In case k is larger than n
rotated_array = elements[-k:] + elements[:-k]

# Print rotated array
print(" ".join(map(str, rotated_array)))


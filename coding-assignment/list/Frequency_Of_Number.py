'''Count the Frequency of Elements
Scenario:
You need to analyze the frequency of keywords in search queries.

Problem Statement:
Write a program to count the frequency of each unique element in an array.

Input Format:

The first line contains an integer n.
The second line contains n space-separated integers.
Output Format:

Print each element and its frequency.
Example:
Input:

8  
4 5 6 5 4 6 5 6
Output:

4: 2  
5: 3  
6: 3'''

# Read input
n = int(input())
elements = list(map(int, input().split()))

# Initialize an empty dictionary to store frequencies
frequency = {}

# Count the frequency of each element
for num in elements:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Print each element and its frequency
for key in sorted(frequency.keys()):
    print(f"{key}: {frequency[key]}")

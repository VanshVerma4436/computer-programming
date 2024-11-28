'''Find the Intersection of Two Arrays
Scenario:
Two research teams are comparing overlapping samples.

Problem Statement:
Write a program to find the intersection of two arrays.

Input Format:

The first line contains an integer n, the size of the first array.
The second line contains n space-separated integers.
The third line contains an integer m, the size of the second array.
The fourth line contains m space-separated integers.
Output Format:

Print the elements in the intersection of the two arrays.
Example:
Input:

5  
1 2 3 4 5  
4  
3 4 5 6
Output:

3 4 5'''

# Read input
n = int(input())
array1 = list(map(int, input().split()))
m = int(input())
array2 = list(map(int, input().split()))

# Find the intersection
intersection = set(array1).intersection(array2)

# Print the intersection elements
print(" ".join(map(str, sorted(intersection))))

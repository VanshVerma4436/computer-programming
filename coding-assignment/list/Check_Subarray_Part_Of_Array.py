''' Check if Array is a Subset of Another
Scenario:
A developer is verifying if a list of required permissions is satisfied by the user's current settings.

Problem Statement:
Write a program to check if an array is a subset of another array.

Input Format:

The first line contains an integer n, the size of the first array.
The second line contains n space-separated integers.
The third line contains an integer m, the size of the second array.
The fourth line contains m space-separated integers.
Output Format:

Print "Yes" if the second array is a subset of the first, otherwise "No."
Example:
Input:

6  
1 2 3 4 5 6  
3  
2 4 6
Output:

Yes'''

# Read input
n = int(input())
array1 = list(map(int, input().split()))
m = int(input())
array2 = list(map(int, input().split()))

# Convert the first array to a set
set_array1 = set(array1)

# Check if all elements of the second array are in the set of the first array
is_subset = all(element in set_array1 for element in array2)

# Print the result
if is_subset:
    print("Yes")
else:
    print("No")

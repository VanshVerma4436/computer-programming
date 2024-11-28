#Find All Permutations of a List : You need to generate all possible permutations of a list of integers.
from itertools import permutations

numbers = [1, 2, 3]
all_permutations = list(permutations(numbers))
print(all_permutations)


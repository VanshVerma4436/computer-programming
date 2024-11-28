#Write a Function to Find the Largest and Smallest Elements in a List : You need to find both the largest and smallest elements in a list of numbers.
def find_largest_smallest(lst):
    return max(lst), min(lst)

largest, smallest = find_largest_smallest([1, 2, 3, 4, 5])
print(f"Largest: {largest}, Smallest: {smallest}")  

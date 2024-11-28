#Write a Function to Find the Intersection of Two Lists : You need to find common elements between two lists.
def find_intersection(list1, list2):
    return list(set(list1) & set(list2))

print(find_intersection([1, 2, 3], [3, 4, 5]))  

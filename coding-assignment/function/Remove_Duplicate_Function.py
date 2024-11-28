#Write a Function to Remove Duplicates from a List : You need to remove duplicate elements from a list.
def remove_duplicates(lst):
    return list(set(lst))

print(remove_duplicates([1, 2, 2, 3, 3, 3]))  

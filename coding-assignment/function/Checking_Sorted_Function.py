#Write a Function to Check if a List is Sorted : You need to check if a list of numbers is sorted in ascending order.
def is_sorted(lst):
    return lst == sorted(lst)

print(is_sorted([1, 2, 3, 4, 5]))  
print(is_sorted([1, 3, 2, 4, 5])) 

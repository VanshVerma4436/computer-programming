#Find the Union of Two Lists: You need to combine two lists of customer IDs without duplicates.
customers1 = [1, 2, 3]
customers2 = [3, 4, 5]
union = list(set(customers1) | set(customers2))
print(union)  

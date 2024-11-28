#Calculate the Sum of Odd Numbers in a List : You have a list of numbers and need to calculate the sum of all odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_of_odds = sum(x for x in numbers if x % 2 != 0)
print(sum_of_odds)  

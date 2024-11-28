#Find the Median of a List : You need to calculate the median value from a list of numbers.
numbers = [1, 3, 3, 6, 7, 8, 9]
numbers.sort()
n = len(numbers)
median = (numbers[n//2] + numbers[(n-1)//2]) / 2
print(median)  

#Write a Function to Count the Frequency of Elements in a List : You need to count the frequency of each element in a list.
def count_frequency(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

print(count_frequency([1, 2, 2, 3, 3, 3])) 

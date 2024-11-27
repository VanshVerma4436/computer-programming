'''Count Frequency of Each Character
Problem: Write a function to count the frequency of each character in a string.

Scenario: You are analyzing text data and need to find the frequency of individual characters.

Example:

Input: "apple"
Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}'''



str = input("Write Any Sentence:")
j = ''
for i in str:
    if i not in j:
     print(end='' f'{i}:{str.count(i)}')
     j += i
   


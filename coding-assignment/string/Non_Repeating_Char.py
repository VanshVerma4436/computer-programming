'''Find the First Non-Repeating Character
Problem: Write a function to find the first non-repeating character in a string.

Scenario: You need to identify the first character in a string that does not repeat.

Example:

Input: "swiss"
Output: "w" '''

word = input("Write Any Fruit:")
empty_str = []
for i in word:
   if word.count(i) == 1:
      empty_str.append(i)
print(empty_str[0])
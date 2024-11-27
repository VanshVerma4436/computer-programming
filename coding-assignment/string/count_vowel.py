'''Count Vowels in a String
Problem: Write a function to count the number of vowels in a string.

Scenario: You are tasked with calculating how many vowels appear in a given sentence.

Example:

Input: "apple"
Output: 2

Input: "python"
Output: 1'''

str = input("Write Any Sentence:")
vowel = ["a","e","i","o","u","A","E","I","O","U"]
count = 0 
for i in str:
    if i in vowel:
     count += 1
print(count)     
      
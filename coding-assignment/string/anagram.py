'''Check if Two Strings are Anagrams
Problem: Write a function to check if two strings are anagrams (i.e., they contain the same characters in different order).

Scenario: You are working on a text processing tool and need to check if two words are anagrams.

Example:

Input: "listen", "silent"
Output: True

Input: "apple", "pale"
Output: False'''

str1 = input("Write Any Sentence:")
str2 = input("Enter Any Sentence:")
ch1 = sorted(str1)
ch2 = sorted(str2)
if(ch1 == ch2):
    print("True")
else:
    print("False")
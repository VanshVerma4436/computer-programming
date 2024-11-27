''' Check if a String is Palindrome
Problem: Write a function to check if a given string is a palindrome.

Scenario: You need to verify if a user-entered string reads the same forward and backward.

Example:

Input: "madam"
Output: True

Input: "hello"
Output: False '''

str = input("Write Any Sentence:").lower()
rev = str[::-1]
if(str == rev):
    print("Given String Is Palindrome.")
else:
    print("Given String Is Not Palindrome.")    
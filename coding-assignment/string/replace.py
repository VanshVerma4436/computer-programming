''' Replace Spaces with %20 (URL Encoding)
Problem: Write a function that replaces all spaces in a string with %20.

Scenario: You are working on URL encoding where spaces must be replaced with %20.

Example:

Input: "hello world"
Output: "hello%20world"'''

str = input("Enter Any Sentence:")
new_str = str.replace(" ","%20")
print(new_str)
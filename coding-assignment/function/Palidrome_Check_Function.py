#Write a Function to Check if a String is a Palindrome : You need to determine if a given string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar")) 

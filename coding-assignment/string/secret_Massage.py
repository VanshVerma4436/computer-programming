'''The Secret Message
Story: A spy has sent you a secret message. The message is a string of characters where all the vowels have been replaced with an asterisk (*). You need to write a program that can recover the original message by replacing the asterisks with vowels in a fixed pattern: a, e, i, o, u.

Problem: Write a Python program that replaces all the asterisks in the input string with vowels, in the order a, e, i, o, u, repeatedly.

Example:

Input:
Th* qu*ck br*wn f*x

Output:
Tha quick brown fox'''


massage = input("Enter your text: ")
vowel = ["a", "e", "i", "o", "u"]
st=''
for i in massage:
    if i in vowel:
        st += "*"
    else:
        st += i
print(st)            
        
       


'''Find the Longest Word in a String
Problem: Write a function to find the longest word in a given sentence.

Scenario: You need to highlight the longest word from a text document.

Example:

Input: "The quick brown fox"
Output: "quick"     '''

sentence=input("Enter Any Sentence:")
word=sentence.split()
empty_List=[]
for i in word:
    empty_List.append(len(i))
longestWord=empty_List.index(max(empty_List))
print(word[longestWord])

'''The Repeated Word Finder
Story: You are reading a large book, and you want to find out which words are repeated the most. Your task is to write a Python program that takes a paragraph of text and prints the most frequent word(s).

Problem: Write a Python program that reads a paragraph and prints the word that appears the most frequently.

Example:

Input:
the quick brown fox jumps over the lazy dog the dog is quick

Output:
the   '''

sentence = input("Write Any Sentence:").lower().split()
count = 0
c = ' '
for i in sentence:
    if sentence.count(i) > 1:
     if i not in c:
        c += i
for i in c:
   print(i,end='')     


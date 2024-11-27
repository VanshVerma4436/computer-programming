'''The Sentence Capitalizer
Story: Your friend has sent you a long email where none of the sentences start with a capital letter. To make the email look nicer, you want to capitalize the first letter of each sentence.

Problem: Write a Python program that takes a paragraph of text and capitalizes the first letter of each sentence.

Example:

Input:
hello. my name is john. i love programming.

Output:
Hello. My name is John. I love programming.'''


text = "hello. my name is john. i love programming."
sentences = text.split('. ')
capitalized_sentences = [sentence.capitalize() for sentence in sentences]
capitalized_text = '. '.join(capitalized_sentences)
print(capitalized_text)

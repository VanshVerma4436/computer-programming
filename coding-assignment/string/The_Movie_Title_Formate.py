'''The Movie Title Formatter
Story: Your friend is creating a website for movies and wants to display all movie titles in title case (where the first letter of each word is capitalized). However, the movie titles are all in lowercase. Your job is to help your friend by writing a program that converts the movie titles to title case.

Problem: Write a Python program that takes a list of movie titles in lowercase and converts them to title case.

Example:

Input:
the lord of the rings harry potter

Output:
The Lord Of The Rings Harry Potter'''


str = input("Enter Movie Titles:")
Movie_Title = str.title()
print(Movie_Title)
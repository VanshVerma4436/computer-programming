'''The Name Reverser
Story: You are working at a name badge company, and you need to print out names in reverse order for a special event. The names are entered as "First Last", and you need to print them as "Last First".

Problem: Write a Python program that takes a list of names in "First Last" format and prints them in "Last First" format.

Example:

Input:
John Doe Alice Johnson

Output:
Doe John Johnson Alice'''


names = input("Enter names: ").split()
reversed_names = []
for i in range(0, len(names), 2):
    first_name = names[i]
    last_name = names[i + 1]
    reversed_names.append(f"{last_name} {first_name}")
print(" ".join(reversed_names))

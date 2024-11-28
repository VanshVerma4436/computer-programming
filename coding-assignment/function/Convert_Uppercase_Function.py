#Write a Function to Convert a List of Strings to Uppercase : You need to convert all the strings in a list to uppercase.
def to_uppercase(lst):
    return [s.upper() for s in lst]

print(to_uppercase(["hello", "world"])) 

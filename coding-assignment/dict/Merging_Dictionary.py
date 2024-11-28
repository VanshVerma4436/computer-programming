#Merging Two Dictionaries : You have two dictionaries with grades from different terms and need to merge them.
term1_grades = {"Vansh": 85, "Arush": 90}
term2_grades = {"Yash": 78, "Rachit": 88}
all_grades = {**term1_grades, **term2_grades}
print(all_grades) 

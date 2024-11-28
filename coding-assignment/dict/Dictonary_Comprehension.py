#Dictionary Comprehension : You need to create a new dictionary with student names and their grades squared.
grades = {"Arush": 85, "Aman": 90, "Arush": 78}
squared_grades = {student: grade**2 for student, grade in grades.items()}
print(squared_grades)  

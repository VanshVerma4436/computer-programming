#Finding the Student with the Highest Grade : You need to determine which student has the highest grade.
grades = {"Aahok": 85, "Rakesh": 90, "Sangam": 78}
best_student = max(grades, key=grades.get)
print(best_student)  

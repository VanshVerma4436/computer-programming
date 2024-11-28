#Creating a Dictionary from Two Lists : You have two lists, one with student names and another with their grades. Create a dictionary from these lists.
names = ["Nimish", "Lakshit", "Akash"]
grades = [85, 90, 78]
students_grades = dict(zip(names, grades))
print(students_grades)  

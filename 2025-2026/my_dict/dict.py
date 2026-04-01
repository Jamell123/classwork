my_dict={}
print(my_dict)
# --- #
student = {'name': 'Alice','age': 20,'major': 'computer science'}
print(student)

print(student['name'])
print(student['age'])

student.update({'age': 21})
print(student)
print(student('gpa'))
student.pop('gpa')
print(student)
print(student.keys())
print(student.values())
print(student.items())
if 'major' in student:
    print(True)
else:
    print(False)
if 'gpa' in student:
    print(True)
else:
    print(False)

inventory = {"apples": 5, "bananas": 3}
print(inventory)


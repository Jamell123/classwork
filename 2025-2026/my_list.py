my_list=[]
print(my_list)

fruits=['apple','banana','orange']
print(fruits)

fruits.append('grape')
fruits.append('mango')
print(fruits)

fruits.insert(2,'kiwi')
print(fruits)

print('first item is ',fruits[0])
print('second item is ',fruits[5])
print('third item is ',fruits[2])

fruits.remove('orange')
print(fruits)

print(fruits)
print(fruits.pop(1))
print(fruits)

numbers=[10, 20, 30, 40, 50]
print(len(numbers))

if 30 in numbers:
    print(True)
else:
    print(False)


if 100 in numbers:
    print(True)
else:
    print(False)

print(numbers[0:3])
print(numbers[:3])
print(numbers[1::3])

colors = ["red", "blue"]
more_colors = ['green',"yellow"]
colors.extend(more_colors)
print(colors)

sources = ['85','92','78','90','88']
sources.sort()
print(sources)
sources.reverse()
print(sources)

letters = ['a','b','a','c','a','b']
letters_count = letters.count('a')
print(letters_count)







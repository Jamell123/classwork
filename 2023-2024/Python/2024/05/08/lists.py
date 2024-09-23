# jamell coleman
# 5/8/2024

# #creating a empty list
lst = []

# using a four loop to add the numbers 1/100 to the list
for py in range(100):
    lst += [py]

# printing the list lst
print(lst)

# using a four loop to add the odd numbers 1/100 to the list
odd = []

# using a four loop to add the odd numbers 1/100 to the odd list
for od in range(1, 101, 2):
    odd.append(od)

# printing the list odd
print(odd)

# using a four loop to add even numbers to the list
even = []

# using a four loop to add the even numbers to the even list
for ev in range(2, 101, 2):
    even.append(ev)

# printing the list even
print(even)

#create a variable named b that points to the first list that you created
b=lst v

#creat a variable named joined that joins the even and odd lists using an operator
joined=odd+even
#Presidents Passwords!

import random

presidentsfile = open("presidents.txt")

list1 = []
list2 = []

for line in presidentsfile:
    newline = line.rstrip("\n1234567890, ")
    newline2 = line.strip("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz\n, ")
    list1.append(newline)
    list2.append(newline2)

number = random.randint(1, len(list1))

password = (list1[number] + list2[number])
print(password)


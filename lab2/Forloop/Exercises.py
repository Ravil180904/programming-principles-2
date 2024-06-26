"""
#Exercise 1. Loop through the items in the fruits list.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#Exercise 2. In the loop, when the item value is "banana", jump directly to the next item.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#Exercise 3. Use the range function to loop through a code set 6 times.

for x in range(6):
    print(x)

#Exercise 4. Exit the loop when x is "banana".

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
""" 
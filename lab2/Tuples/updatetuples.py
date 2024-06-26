#1. Convert the tuple into a list to be able to change it:
"""
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
"""

#2. Convert the tuple into a list, add "orange", and convert it back into a tuple:
"""
thistuple = ("apple", "banana", "cherry",)
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
"""

#3. Create a new tuple with the value "orange", and add that tuple:
"""
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
"""

#4. Convert the tuple into a list, remove "apple", and convert it back into a tuple:
"""
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y) 
print(thistuple)
"""

#5. The del keyword can delete the tuple completely:
"""
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) # This will raise an error because the tuple no longer exists
"""

"""
#Exercise 1. Print i as long as i is less than 6.
i = 1
while i < 6:
    print(i)
    i += 1

#Exercise 2. Stop the loop if i is 3 

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#Exercise 3. In the loop, when i is 3, jump directly to the next iteration.

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#Exercise 4. Print a message once the condition is false.

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer then  6")
"""

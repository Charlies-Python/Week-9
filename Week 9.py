print("Before fix:")
n = 100
i = 0
while i**2<=n:
    if i % 2 == 0:
        i = i**2
        print(i)
    i = i + 1
print("After fix:")
i = 0
n = 100
while i**2<=n:
    if i % 2 == 0:
        x = i**2
        print(x)
    i = i+1
print("Exercise 2:")
i = 0
n = int(input ("Please enter a number: "))
while i**2<=n:
    if i % 2 == 0:
        x = i**2
        print(x)
    i = i+1
print("Exercise 3: ")
need_input = True
while need_input:
    try:
        i = 0
        n = int(input("Please enter a positive integer: "))
        if n>0:
            need_input = False
    except IndexError:
        print("Try again.")
while i**2<=n:
    if i % 2 == 0:
        x = i**2
        print(x)
    i = i+1

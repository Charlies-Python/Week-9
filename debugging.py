i = 35
counter = 0
while 1<i:
    counter = counter + 1
    print(i)
    if i%2 == 0:
        i = i/2
    else:
        i = 3*i + 1
print(f"In the end, i={i}.")
print(f"After {counter} loops, i={i}.")
print("Exercise 1")
fahrenheit = 45.5
celsius = (fahrenheit-32)*5/9
print(celsius)
print("Exercise 2")
data = [10, 20, 30, 40]
total = sum(data)
average = total/len(data)
print(average)
print("Exercise 3")
from random import randint
n = randint(1,2)
if n == 2:
    print("heads")
else:
    print("tails")
print("Exercise 4")
numbers = [5, 3, -2, 8, -1]
for n in numbers:
    if n<0:
        print(n)
        break
    else:
        print()
print("Exercise 5")
i = 1
while i<=100:
    print(i)
    x = i**2
    print(x)
    i = i+1

Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
warning = "Winter is coming"
print(warn)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(warn)
NameError: name 'warn' is not defined
print(warning)
Winter is coming
x = 4
for vowel in ("a", "e", "i", "o", "u"):
    x = vowel
if x>3:
    
SyntaxError: invalid syntax
if x>3:
    print("Hurrah!")

Hurrah!
i=35
while i<1:
    if i%2 == 0:
        i=i/2
    i = 3*i+1
print(f"In the end, i={i}.")
SyntaxError: invalid syntax
print(f"In the end, i={i}.")
In the end, i=35.
i=35
while i<1:
    print("bananas")
    if i% 2 ==0:
        i = i/2
    i = 3*i+1
print(f"In the end, i={i}.")
SyntaxError: invalid syntax
print(f"In the end, i={i}.")
In the end, i=35.
i=35 while 1<i<10000000000000000000:
    
SyntaxError: invalid syntax
i=35
while 1<i<1000000000000000:
    print("Bananas")
    if i%2==0
    
SyntaxError: expected ':'
while 1<i<1000000000000000:
    print("Bananas")
    if i%2==0:
        i=i/2
    i=3*i+1
print(f"In the end, i={i}.")
SyntaxError: invalid syntax
print(f"In the end, i={i}.")
In the end, i=35.
i=35
while 1<i<10000:
    print("bananas")
    if i%2 == 0:
        i=i/2
    i=3*i+1
print(f"In the end, i={i}")
SyntaxError: invalid syntax
print(f"In the end, i={i}")
In the end, i=35
i=35
while 1<i<10000:
    print("bananas")
    if i % 2 == 0:
        i = i/2
    i = 3*i + 1
print(f"In the end, i={i}.")
SyntaxError: multiple statements found while compiling a single statement
i=35
while 1<i<10000:
    print("bananas")
    if i % 2 == 0:
        i = i/2
    i = 3*i + 1
print(f"In the end, i={i}.")
SyntaxError: invalid syntax
print(f"In the end, i={i}.")
In the end, i=35.
i=35
while 1<i<10000:
    print("bananas")
    if i % 2 == 0:
        i = i/2
    i = 3*i + 1
print(f"In the end, i={i}.")
SyntaxError: invalid syntax
print(f"In the end, i={i}.")
In the end, i=35.
print(f"In the end, i={i}.")
In the end, i=35.

i=35
while 1<i<10000:
    print("bananas")
    if i % 2 == 0:
        i = i/2
    else i = 3*i + 1
    
SyntaxError: expected ':'
while 1<i<10000:
    print("bananas")
    if i % 2 == 0:
        i = i/2
    else:
        i = 3*i + 1
print (f"In the end, i={i}.")
SyntaxError: invalid syntax

print (f"In the end, i={i}.")
In the end, i=35.
i=35
while 1<i<10000:
    print(i)
    if i % 2 == 0:
        i = i/2

    i = 3*i + 1
print(f"In the end, i={i}.")
SyntaxError: multiple statements found while compiling a single statement
i = 35
while 1<i<10000:
    print(i)
    if i % 2 == 0:
        i = i/2
        
    i = 3*i + 1
print(f"In the end, i={i}.")
SyntaxError: invalid syntax
print(f"In the end, i={i}.")

In the end, i=35.
In the end, i=35.
SyntaxError: invalid syntax

======= RESTART: C:/Users/c6011234/Desktop/debugging code.py =======
35
106
160.0
241.0
724.0
1087.0
3262.0
4894.0
7342.0
In the end, i=11014.0.

======= RESTART: C:/Users/c6011234/Desktop/debugging code.py =======
35
106
160.0
241.0
724.0
1087.0
3262.0
4894.0
7342.0
In the end, i=11014.0.
106
53.0
160.0
In the end, i=160.0.

======= RESTART: C:/Users/c6011234/Desktop/debugging code.py =======
35
106
160.0
241.0
724.0
1087.0
3262.0
4894.0
7342.0
In the end, i=11014.0.
106
53.0
160.0
In the end, i=160.0.
New loop
35
106
In the end, i=106.
New loop
106
53.0
In the end, i=53.0.
New loop
53.0
160.0
In the end, i=160.0.

======= RESTART: C:/Users/c6011234/Desktop/debugging code.py =======
35
106
160.0
241.0
724.0
1087.0
3262.0
4894.0
7342.0
In the end, i=11014.0.
106
53.0
160.0
In the end, i=160.0.
New loop
35
106
In the end, i=106.
New loop
106
53.0
In the end, i=53.0.
New loop
53.0
160.0
In the end, i=160.0.
35
106
53.0
160.0
80.0
40.0
20.0
10.0
5.0
16.0
8.0
4.0
2.0
In the end, i=1.0.

======= RESTART: C:/Users/c6011234/Desktop/debugging code.py =======
35
106
160.0
241.0
724.0
1087.0
3262.0
4894.0
7342.0
In the end, i=11014.0.
106
53.0
160.0
In the end, i=160.0.
New loop
35
106
In the end, i=106.
New loop
106
53.0
In the end, i=53.0.
New loop
53.0
160.0
In the end, i=160.0.
35
106
53.0
160.0
80.0
40.0
20.0
10.0
5.0
16.0
8.0
4.0
2.0
In the end, i=1.0.
35
106
53.0
160.0
80.0
40.0
20.0
10.0
5.0
16.0
8.0
4.0
2.0
After 13 loops, i=1.0.

======= RESTART: C:/Users/c6011234/Desktop/debugging code.py =======
35
106
160.0
241.0
724.0
1087.0
3262.0
4894.0
7342.0
In the end, i=11014.0.
106
53.0
160.0
In the end, i=160.0.
New loop
35
106
In the end, i=106.
New loop
106
53.0
In the end, i=53.0.
New loop
53.0
160.0
In the end, i=160.0.
35
106
53.0
160.0
80.0
40.0
20.0
10.0
5.0
16.0
8.0
4.0
2.0
In the end, i=1.0.
35
106
53.0
160.0
80.0
40.0
20.0
10.0
5.0
16.0
8.0
4.0
2.0
After 13 loops, i=1.0.
Traceback (most recent call last):
  File "C:/Users/c6011234/Desktop/debugging code.py", line 53, in <module>
    celsius = (fahrenheit - 32) * 5/9
NameError: name 'fahrenheit' is not defined. Did you mean: 'fahrenheint'?

======= RESTART: C:/Users/c6011234/Desktop/debugging code.py =======
35
106
160.0
241.0
724.0
1087.0
3262.0
4894.0
7342.0
In the end, i=11014.0.
106
53.0
160.0
In the end, i=160.0.
New loop
35
106
In the end, i=106.
New loop
106
53.0
In the end, i=53.0.
New loop
53.0
160.0
In the end, i=160.0.
35
106
53.0
160.0
80.0
40.0
20.0
10.0
5.0
16.0
8.0
4.0
2.0
In the end, i=1.0.
35
106
53.0
160.0
80.0
40.0
20.0
10.0
5.0
16.0
8.0
4.0
2.0
After 13 loops, i=1.0.
7.5

Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from sympy import *
hello = 5
print
print(hello)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(hello)
NameError: name 'hello' is not defined. Did you mean: 'help'?
hello = 5
print(hello)
5
from sympy.abc import x,y,z,t
f = x**2
f.subs(x, 4)
16
f = x**7 + 3 * x**5 + 9
diff(f,x)
7*x**6 + 15*x**4
diff(cos(t)**3 + sint(t)**2, t)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    diff(cos(t)**3 + sint(t)**2, t)
NameError: name 'sint' is not defined. Did you mean: 'int'?
diff(cos(t)**3 + sin(t)**2, t)
-3*sin(t)*cos(t)**2 + 2*sin(t)*cos(t)
f = 25*x**6 + 78*x**5 - 45*x**4
solve(diff(f,x))
[-3, 0, 2/5]
f.subs(x,-3)
-4374
f = 2*x*y**2
f = 2*x*z+y**2+sin(x*z)
f.subs([(x,2), (y,4), (z,1)])
sin(2) + 20
f.subs([(x, 2), (y,4), (z,1)]).evalf()
20.9092974268257
f = x**7*y**3*z**4 + 3*x**5 * z + 9*y*z + 7
diff(f,x)
7*x**6*y**3*z**4 + 15*x**4*z
diff(f,y)
3*x**7*y**2*z**4 + 9*z
diff(f,z)
4*x**7*y**3*z**3 + 3*x**5 + 9*y
diff(f,x,2)
6*x**3*z*(7*x**2*y**3*z**3 + 10)
>>> diff(f,y,2)
6*x**7*y*z**4
>>> diff(f,z,2)
12*x**7*y**3*z**2
>>> diff(f,x,y)
21*x**6*y**2*z**4
>>> diff(f,y,x)
21*x**6*y**2*z**4
>>> f = t**2 * cos(t)
>>> integrate(f,t)
t**2*sin(t) + 2*t*cos(t) - 2*sin(t)
>>> integrate(f,[t,2*pi,9/4*pi])
-4*pi - sqrt(2) + 2.25*sqrt(2)*pi + 2.53125*sqrt(2)*pi**2
>>> integrate(f,[t,2*pi,9/4*pi]).evalf()
31.3464024447959
>>> limit((x**2-4)/(x**2-5*x+6),x,2)
-4
>>> limit((1+1/x)**x,x,oo)
E
>>> limit(1/(x-3),x,3)
oo
>>> from sympy.abc import h
>>> f = x**2
>>> f.subs(x,x+h)
(h + x)**2
>>> limit((f.subs(x,x+h)-f)/h,h,0)
2*x
>>> f=3*cos(4*x+pi)+exp(-2*x)
>>> limit((f.subs(x,x+h)-f)/h,h,0)
(12*exp(2*x)*sin(4*x) - 2)*exp(-2*x)
>>> diff(f,x)
12*sin(4*x) - 2*exp(-2*x)
>>> simplify(limit((f.subs(x,x+h)-f/h,h,0)))
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    simplify(limit((f.subs(x,x+h)-f/h,h,0)))
TypeError: limit() missing 2 required positional arguments: 'z' and 'z0'
>>> simplify(limit((f.subs(x,x+h) - f)/h,h,0))
12*sin(4*x) - 2*exp(-2*x)

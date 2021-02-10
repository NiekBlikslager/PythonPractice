# my attempt at the PythonPractice problem
a = b = c = 0
d = ''
for i in range(101):
    if i % 3 == 0:
        a = 1
    if i % 5 == 0:
        b = 1
    if i % 7 == 0:
        c = 1
    if a == 1 or b == 1 or c == 1:
        d = ''
    else:
        d = i

    print(a*"Fizz", b*"Buzz", c*"Foo", d, sep='')
    a = b = c = 0
    d = ''

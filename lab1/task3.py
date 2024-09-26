import math
a = 0.1
b = 1.0
h = 0.1
pes = 0.0001
x = a
while x <= b:
    o = x * x
    y = (1 + 2 * o) * math.exp(o)
    i = 0
    sum = 0
    term = 1
    while abs(term) >= pes:
        term = ((2 * i + 1) * (x ** (2 * i))) / math.factorial(i)
        sum += term
        i += 1
    print('x =',x, ';', 'Сумма =',sum, ';', 'y =',y)
    x += h
    
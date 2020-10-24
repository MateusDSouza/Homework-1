import numpy
n, m = map(int,input().split())
a, b =(numpy.array([input().split() for i in range(n)], dtype=int) for j in range(2))
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)

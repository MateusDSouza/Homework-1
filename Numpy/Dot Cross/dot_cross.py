import numpy
#numpy.set_printoptions(sign=' ',legacy='1.13')
w = int(input())
a=numpy.array([input().split() for _ in range(w)],int)
b=numpy.array([input().split() for _ in range(w)],int)
aux=numpy.dot(a,b)
print(aux)
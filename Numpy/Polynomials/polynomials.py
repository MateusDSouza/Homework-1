import numpy
a=numpy.array(input().split(),float)
b=int(input())
aux=numpy.polyval(a,b)
print(aux)

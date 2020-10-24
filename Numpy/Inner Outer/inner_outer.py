import numpy
#numpy.set_printoptions(sign=' ',legacy='1.13')
a=numpy.array(input().split(),int)
b=numpy.array(input().split(),int)
aux=numpy.inner(a,b)
print(aux)
aux2=numpy.outer(a,b)
print(aux2)
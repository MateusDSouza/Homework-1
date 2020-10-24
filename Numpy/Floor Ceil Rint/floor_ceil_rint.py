import numpy
numpy.set_printoptions(sign=' ')
a=numpy.array(input().split(),dtype=float)
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))
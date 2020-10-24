import numpy
w,e =map(int,input().split())
a=numpy.array([input().split() for _ in range(w)],int)
aux=numpy.sum(a,0)
aux2=numpy.prod(aux,0)
print(aux2)

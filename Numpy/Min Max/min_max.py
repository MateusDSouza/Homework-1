import numpy
w,e =map(int,input().split())
a=numpy.array([input().split() for _ in range(w)],int)
aux=numpy.min(a,1)
aux2=numpy.max(aux,0)
print(aux2)
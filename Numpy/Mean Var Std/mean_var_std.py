import numpy
numpy.set_printoptions(sign=' ',legacy='1.13')
w,e =map(int,input().split())
a=numpy.array([input().split() for _ in range(w)],int)
aux=numpy.mean(a,1)
print(aux)
aux2=numpy.var(a,0)
print(aux2)
aux3=numpy.std(a)
print(aux3)
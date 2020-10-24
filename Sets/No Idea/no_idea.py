# Enter your code here. Read input from STDIN. Print output to STDOUT
tam=[]
tam=input().split()
tam = list(map(int,tam))
#print(tam)
n=[]
n=input().split()
n = list(map(int,n))
#print(n)
a=[]
a=input().split()
a = list(map(int,a))
a=set(a)
#print(a)
b=[]
b=input().split()
b = list(map(int,b))
#print(b)
b=set(b)
#print(b)
out=0
for i in range(0,len(n)):
    if n[i] in a:
        out+=1
    elif n[i] in b:
        out-=1
    #print(out)    
print(out)
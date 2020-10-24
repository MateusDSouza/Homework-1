n = int(input())
s = set(map(int, input().split()))
m=int(input())
for i in range(0,m):
    aux=input().split()
    if (aux[0]=='pop'):
        s.pop()
    elif (aux[0]=='discard'):
        s.discard(int(aux[1]))
    elif (aux[0]=='remove'):
        s.remove(int(aux[1]))
print(sum(s))
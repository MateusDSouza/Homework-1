from collections import deque
n = int(input())
s = deque()
for i in range(0,n):
    comando=input().split()
    if (comando[0]=='append'):
        s.append(int(comando[1]))
    elif (comando[0]=='pop'):
        s.pop()
    elif (comando[0]=='popleft'):
        s.popleft()
    elif (comando[0]=='appendleft'):
        s.appendleft(comando[1])

print(*[i for i in s])
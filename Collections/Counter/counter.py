# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x=int(input())
shoes=map(int,input().split())
organized=Counter(shoes)
n=int(input())
dinheiro = []
for _ in range (n):
    size,value =map(int,input().split())
    if (organized[size] > 0):
        dinheiro.append(value)
        organized.subtract(Counter([size]))
print(sum(dinheiro))
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d = defaultdict(list)
x=[]

n, m = map(int,input().split())

for i in range(0,n):
    d[input()].append(i+1) 

for i in range(0,m):
    x=x+[input()]  

for i in x: 
    if i in d:
        print (" ".join( map(str,d[i]) ))
    else:
        print (-1)
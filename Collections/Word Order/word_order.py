# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter, OrderedDict
n=int(input())
d=OrderedDict()
for _ in range(n):
    word = input()
    d.setdefault(word, 0)
    d[word] += 1
   
print(len(d))
print(*d.values())

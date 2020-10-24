# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
#print(m)
a=set(map(int,input().split()))
#print(a)
n=int(input())
#print(n)
b=set(map(int,input().split()))
#print(b)
#do the math
num1=a.symmetric_difference(b)
#num2=a.intersection(b)
#result = num1.difference(num2)
print(len(num1))
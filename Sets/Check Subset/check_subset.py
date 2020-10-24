# Enter your code here. Read input from STDIN. Print output to STDOU
num_test=int(input())
for i in range(0,num_test):
    num_element_a=int(input())
    a=set(map(int,input().split()))
    num_element_b=int(input())
    b=set(map(int,input().split()))
    print(a.issubset(b))
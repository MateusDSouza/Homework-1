a=set(map(int,input().split()))
num_subset_n=int(input())
for i in range(0,num_subset_n):
    n=set(map(int,input().split()))
    if (a.issuperset(n)):
        resultado=True
    else:
        resultado = False
        break
print(resultado)
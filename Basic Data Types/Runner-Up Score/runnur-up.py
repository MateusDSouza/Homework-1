if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    primo=max(arr)
while max(arr)==primo:
    arr.remove(max(arr))
    segundo=max(arr)        
print(segundo)

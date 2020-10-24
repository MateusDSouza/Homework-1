def average(array):
    array = list(dict.fromkeys(array))
    aux=sum(array)
    aux2=len(array)
    return aux/aux2
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
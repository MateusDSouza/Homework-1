cube = lambda x: pow(x,3)# complete the lambda function 

def fibonacci(y):
    fib = [0,1]
    if (y < 2): lambda y: y
    if(n>1):
        for i in range(2,y):
            fib.append(fib[i-2]+fib[i-1])
  #  elif (n==1):
    #    return (fib[0:1])
   # elif (n==0):
     #   return (None)
    return (fib[:y])
    # return a list of fibonacci numbers


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
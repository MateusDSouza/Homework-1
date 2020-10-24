if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())

    listax=[i for i in range(x+1)]
    listay=[j for j in range(y+1)]
    listaz=[k for k in range(z+1)]
    perm = [[a,b,c] for a in listax for b in listay for c in listaz if a+b+c!=n]
    print perm
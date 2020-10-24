if __name__ == '__main__':
    n = int(input())
    l = []
    for i in range(n):
        s = input().split()
        command = s[0]
        args = s[1:]
        if command=="insert":
            l.insert(int(args[0]),int(args[1]))
        elif command=="remove":
            l.remove(int(args[0]))
        elif command=="append":
            l.append(int(args[0]))
        elif command=="sort":
            l.sort()
        elif command=="pop":
            l.pop()
        elif command=="reverse":
            l.reverse()
        elif command=="print":
            print(l)
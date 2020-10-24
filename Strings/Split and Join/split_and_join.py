def split_and_join(line):
    # write your code here
    x = line.split(" ")
    x2="-".join(x)
    return x2
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
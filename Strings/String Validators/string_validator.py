if __name__ == '__main__':
    s = input()
    for i in range(len(s)):
        sub=s[i]
        if sub.isalnum():
            print(sub.isalnum())
            break
    if(sub.isalnum()!=True):
        print(sub.isalnum())    
    for i in range(len(s)):
        sub=s[i]
        if sub.isalpha():
            print(sub.isalpha())
            break
    if(sub.isalpha()!=True):
        print(sub.isalpha())     
    for i in range(len(s)):
        sub=s[i]
        if sub.isdigit():
            print(sub.isdigit())
            break
    if(sub.isdigit()!=True):
        print(sub.isdigit())     
    for i in range(len(s)):
        sub=s[i]
        if sub.islower():
            print(sub.islower())
            break
    if(sub.islower()!=True):
        print(sub.islower()) 
    for i in range(len(s)):
        sub=s[i]
        if sub.isupper():
            print(sub.isupper())
            break
    if(sub.isupper()!=True):
        print(sub.isupper())     
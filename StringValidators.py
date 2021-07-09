if __name__ == '__main__':
    s = input()
    a=True
    for i in s:
        if i.isalnum()==True:
            a=True
            print(a)
            break
    else:
        a=False
        print(a)
        
    for i in s:
        if i.isalpha()==True:
            a=True
            print(a)
            break
    else:
        a=False
        print(a)
    for i in s:
        if i.isdigit()==True:
            a=True
            print(a)
            break
    else:
        a=False
        print(a)
    for i in s:
        if i.islower()==True:
            a=True
            print(a)
            break
    else:
        a=False
        print(False)
    for i in s:
        if i.isupper()==True:
            a=True
            print(a)
            break
    else:
        a=False
        print(a)

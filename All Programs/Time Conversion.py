def func():
    c=input()
    d=c[0:8]
    list1=list(map(str,d.split(':')))
    r=c[len(c)-2]
    if r=='P':
        if list1[0]!='12':
            list1[0]=str(int(list1[0])+12)
        else:
            list1[0]='12'
    else:
        if list1[0]=='12':
            list1[0]='00'
    print(':'.join(list1))
func()

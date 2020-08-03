def func():
    x=int(input(""))
    y=int(input(""))
    z=int(input(""))
    n=int(input(""))
    list1=[]
    list2=[]
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                if i+j+k!=n:
                    list2.append(i)
                    list2.append(j)
                    list2.append(k)
                    list1.append(list2)
                    list2=[]
    print(list1)
func()
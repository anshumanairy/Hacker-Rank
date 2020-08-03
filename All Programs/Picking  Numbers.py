def func():
    n=int(input())
    list1=list(map(int,input().split()))
    list1.sort()
    list2=list(set(list1))
    if len(list2)!=1:
        list3=[]
        for i in list2:
            list3.append(list1.count(i))
        list4=[]
        for i in range(len(list2)-1):
            if abs(list2[i+1]-list2[i])<=1:
                list4.append(list3[i+1]+list3[i])
        print(max(list4))
    else:
        print(n)
func()

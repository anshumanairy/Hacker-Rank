def func():
    n=int(input())
    list2=[]
    list3=[]
    for i in range(0,n):
        c=input()
        list1=list(map(str,c.split()))
        avg=(float(list1[1])+float(list1[2])+float(list1[3]))/3
        avg=format(avg,'.2f')
        list2.append(avg)
        list3.append(list1[0])
    d=input()
    for j in range(0,n):
        if list3[j]==d:
            print(list2[j])
func()


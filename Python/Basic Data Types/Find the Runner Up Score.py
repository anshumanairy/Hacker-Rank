def func():
    n=int(input())
    list1=list(set(list(map(int,input().split()))))
    list1.sort()
    print(list1[-2])
func()
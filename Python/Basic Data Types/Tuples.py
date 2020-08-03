def func():
    n=int(input())
    c=input()
    list1=tuple(list(map(int,c.split())))
    print(hash(list1))
func()
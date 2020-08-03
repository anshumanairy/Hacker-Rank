def func():
    q=int(input())
    for i in range(q):
        x,y,z=map(int,input().split())
        a=abs(z-x)
        b=abs(z-y)
        if a==b:
            print("Mouse C")
        elif a<b:
            print("Cat A")
        else:
            print("Cat B")
func()

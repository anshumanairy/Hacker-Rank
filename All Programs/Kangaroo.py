def func():
    x1,v1,x2,v2=map(int,input().split())
    if x1<x2:
        if v1>v2:
            if abs(x1 - x2) % abs(v2 - v1) == 0:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        if v2>v1:
            if abs(x1 - x2) % abs(v2 - v1) == 0:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
func()

def func():
    n=int(input())
    for i in range(n):
        x=int(input())
        if x>37:
            if x%5>=3:
                print(x+(5-(x%5)))
            else:
                print(x)
        else:
            print(x)
func()

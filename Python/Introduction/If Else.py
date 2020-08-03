def func():
    n = int(input())
    if n%2!=0:
        print("Weird")
    else:
        if n>=2 and n<6:
            print("Not Weird")
        if n>=6 and n<21:
            print("Weird")
        if n>=21:
            print("Not Weird")
func()
def func():
    n=int(input())
    s=list(set(list(map(int,input().split()))))
    s.sort()
    m=int(input())
    a=list(map(int,input().split()))
    list1=[]
    j=0
    for i in a:
        while j<len(s) and i>=s[j]:
            j=j+1
        list1.append(len(s)+1-j)
         
    print(*list1,sep='\n')
func()

def func():
    n,m=map(int,input().split())
    var=".|."
    x=1
    y=1
    for i in range(n):
        list1=[]
        count=0
        for j in range(m):
            if i==(n//2):
                y=x
                if j<((m//2)-3) or j>((m//2)+3):
                    list1.append('-')
                if j==m//2:
                    list1.append("WELCOME")
            elif i<(n//2):
                if (j<=(m//2)-((i+1)*3)+1) or (j>=(m//2)+((i+1)*3)-1):
                    list1.append('-')
                else:
                    if count<x:
                        count+=1
                        list1.append(var)
            else:
                if (j<=(m//2)-((n-i)*3)+1) or (j>=(m//2)+((n-i)*3)-1):
                    list1.append('-')
                else:
                    if count<y:
                        count+=1
                        list1.append(var)
        x+=2
        y-=2
        print(*list1,sep='')
func()

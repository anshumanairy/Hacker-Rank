if __name__ == '__main__':
    n = int(input())
    list1=[""]*n
    j=0
    for i in range(1,n+1):
        list1[j]=i
        j+=1
    print(*list1,sep='')


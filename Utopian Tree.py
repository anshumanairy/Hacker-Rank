def utopianTree():
    n=int(input())
    i=0
    j=1
    while i<n:
        if i%2==0:
            j*=2
        else:
            j+=1
        i+=1
    print(j)
utopianTree()

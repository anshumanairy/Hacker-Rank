T = int(input())
ans = []
for x in range (T):
    n = int(input())
    y = input()
    z = list(map(int, y.split()))
    new = []
    
    for a in range(len(z)):
        if z[0]>=z[-1]:
            new.append(z[0])
            z.pop(0)
        else:
            new.append(z[-1])   
            z.pop() 
    
    for x in range(1, len(new)+1):
        if new[x]>new[x-1]:
            ans.append('No')
            break
        else:
            if x==len(new)-1:
                ans.append('Yes')
            
                break
                
print(*ans, sep = '\n')               


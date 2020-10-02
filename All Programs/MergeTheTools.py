from collections import OrderedDict
def merge_the_tools(string, k):
    # your code goes here
    i=0
    l=[]
    while(i<len(string)):
        m="".join(OrderedDict.fromkeys(string[i:i+k]))
        l.append(m)
        i=i+k
    print (*l,sep="\n")  

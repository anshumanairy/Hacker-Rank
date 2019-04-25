  def func():
    h=input()
    word=input()
    list1=list(map(int,h.split()))
    list2=list(word)
    list3=[]
    for i in range(len(list2)):
        x=list2[i]
        list3.append(list1[ord(x)-97])
    c=max(list3)
    print(len(list2)*c)
func()

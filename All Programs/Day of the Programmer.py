import calendar
import datetime
def func():
    y=int(input())
    x=13
    z=9
    if y<1918:
        if y%4==0:
            x=x-1
    elif y==1918:
        x=26
    else:
        if y%4==0 and y%100!=0 or y%400==0:
            x=x-1
    list3=[]
    list3.append(str(x))
    if len(str(z))==1:
        list3.append(str(z).zfill(2))
    else:
        list3.append(str(z).zfill(2))
    list3.append(str(y))
    print('.'.join(list3))
func()

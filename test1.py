def tarkastus(lista):
    for x in range(0,len(lista)):
        if(lista[x]>9 or lista[x]<0):
            return False 
    for x in range(0,len(lista)):
        for y in range(0,len(lista)):
            if(x!=y and lista[x]==lista[y]):
                return False
                
    return True

s=1
l=9
o=0
arvo=True
for i in range(2,9):
    list0=[s,l,o]
    e=19-2*i 
    a=9-i 
    list1=1*list0
    list1.append(i)
    list1.append(e)
    list1.append(a)
    print(list0,list1)
    for m in range(2,9): 
        list2=1*list1
        d=m-1
        list2.append(m)
        list2.append(d)
        for r in range(2,9):
            list3=1*list2
            f=2+r+d
            list3.append(r)
            list3.append(f)
            arvo=tarkastus(list3)
            if(arvo==True):
                print("BREAK")
                break
            else:
                list3.remove(r)
                list3.remove(f)
        if(arvo==True):
            print("BREAK")
            break
        else:
            list3.remove(m)
            list3.remove(d)
    if(arvo==True):
        print("BREAK")
        break  
    else:
        list3.remove(i)
        list3.remove(e)
        list3.remove(a)          
                
print(list3)
                
                
                
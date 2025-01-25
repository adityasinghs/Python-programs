l1=[]
l2=[]
l3=[]
c=0
l=0
lsize=int(input("Enter size of tuple :  "))
while (c<lsize):
    
    l=int(input("Enter values :"))
    l1.append(l)
    
    cube=l**3
    #print(cube)
    
    l2.insert(0,l)
    l2.insert(1,cube)

    #t1=tuple(l2)
    #print(t1)
    l3.append(tuple(l2))
    c+=1
    l2=[]
    
print(l3)

    


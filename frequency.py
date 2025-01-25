l1=[]
lsize=int(input("Enter size of tuple :  "))
c=0
while (c<lsize):
    
    l=int(input("Enter values :"))
    l1.append(l)
    t1=tuple(l1)
    c+=1
a=0
for i in t1:
    a=t1.count(i)
    print("Frequency of ",i,' is ',a) 
    

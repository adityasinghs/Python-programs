#largest number

#user defined list
l1=[]
n=int(input("Enter size of list :"))
c=0     
while(c<n):
    l=int(input("Enter element :"))
    l1.append(l)
    c+=1
#finding largest number
c=0
largest=l1[c]

d=1
for i in l1:
    if (i!=l1[-1]):
        if (largest<l1[c+1]):
            largest=l1[c+1]
            c+=1

        else:
            largest=l1[c]
            c+=1
print("Largest eleement of the list : ",largest)

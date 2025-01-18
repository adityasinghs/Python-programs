lsize=int(input("Enter size of list  "))
l1=[]
c=0
while (c<lsize):
    c+=1
    l=int(input("Enter values :"))
    l1.append(l)
print("List given by use :",l1)
print("Choose from the following : ")
print("a: Count total no of the element of list ")
print("b: Reverse the element of the list ")
print("c: Delete a particular element  given by user")
print("d: Sort the element of the list ")

b1=0
u=input("Enter ")

if (u=="a"):
    for i in l1:
        b1+=1
    print(b1)

elif (u=="b"):
    l1.reverse()
    print("Reversed list : ",l1)

elif (u=="c"):
    d=int(input("Enter which element to delete : "))
    l1.remove(d)
    print("After deletionof element :",l1)

elif (u=="d"):
    l1.sort()
    print("Sorted list :",l1)

else:
    print("Enter valid option ")
        
    
    

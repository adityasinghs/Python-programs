#wap to create two userdefined list of same order and at their corresponding elements
#user defined lists
l1=[]
l2=[]
n=int(input("Enter size of list :"))
c=0     
while(c<n):
    l=int(input("Enter element :"))
    l1.append(l)
    l2.append(l)
    c+=1

print("List 1 elements",l1)

print("List 2 elements",l2)

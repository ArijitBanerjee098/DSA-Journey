n1=int(input("Enter the number: "))
n2=int(input("Enter the number: "))
ans=0
c=min(n1,n2)
for i in range(1,c):
    if n1%i==0 and n2%i==0:
        ans=i
print(ans)        
        




                                
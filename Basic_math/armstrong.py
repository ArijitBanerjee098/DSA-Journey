n=int(input("Enter the number: "))
temp=n
sum=0
while n>0:
    d=n%10
    sum=sum+(d*d*d)
    n=n//10
if sum==temp:
    print("Armstrong number")
else:
    print("Not Armstroong number")


    
    
        
    
    
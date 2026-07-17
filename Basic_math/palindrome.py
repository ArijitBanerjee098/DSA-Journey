n=int(input("Enter the num: "))
rev=0
temp=n
while n>0:
    digit=n%10
    n=n//10
    rev=(rev*10)+digit
if rev==temp:
    print("True")
else:
    print("False")
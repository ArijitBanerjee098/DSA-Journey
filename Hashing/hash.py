def cou():
    count=0
    arr=[1,3,4,1,3,5]
    n=int(input("The element: "))
    for i in arr:
        if i==n:
            count=count+1
    print("The element have in array: ", count)
cou()    



# usimg Hash array

arr = list(map(int, input().split())) #take arr elements in a list
print(arr)
 
# one more process take elemnts throw a loop
arr=[]
n=int(input("How many times: " ))
for i in range(n):
    j=int(input("Enter elements: "))
    arr.append(j)
print(arr) 

hashlist=[0]*13

for i in arr:
    hashlist[i]+=1
print(hashlist)    


q = int(input("Times: "))
for i in range(q):
    number = int(input("enter Numbers: "))
    print(hashlist[number])




#clear process of hash frequency
arr=[2,4,5,2,5]  #array

hashlist=[0]*8  #take a 8 index array elemets are zero

for i in arr: #this is a loop for arr
    
    hashlist[i]+=1
    #here is most important my array numbers will be save hashlist index throw count. like my arr index 0 number is 2. Here in Hashlist array 2 index count 0+1=1 

print(hashlist) #here hashlist print [0, 0, 2, 0, 1, 2, 0, 0]

t=int(input("Enter time:  ")) #here take a input number

for j in range(t): #Here loop will be run given input t
    
    e=int(input("Enter elements: ")) #Here take elements
    
    print(hashlist[e]) #and last here print given elements how many time here throw hashlist array
       
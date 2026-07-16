# k=ord("A")
# print(k)
# print(chr(k))

def chr16(n):
    for i in range(n):
        k=ord("A")
        for j in range(i+1):
            print(chr(k), end=" ")
            k+=1
        print()    
chr16(5)        
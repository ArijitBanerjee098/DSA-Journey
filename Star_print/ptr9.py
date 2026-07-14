def str9(n):
    for i in range(0,n):
        for j in range(0, n-i-1):
            print(end=" ")
        for j in range(1, i+1):
            print(j, end=" ")
        print()
str9(5)                
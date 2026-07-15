def str12(n):
    num=1
    for i in range(n):
        for j in range(i):
            print(num, end=" ")
            num+=1
        print()
str12(6)            
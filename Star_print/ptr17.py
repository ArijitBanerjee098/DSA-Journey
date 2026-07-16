for i in range(1,6):
    for j in range(1, i+1):
        print("*", end=" ")
    for s in range(1, (5-i)*2+1):
        print(" ", end=" ")
    for j in range(1, i+1):
        print("*", end=" ")
    print()
for i in range(4,0,-1):
    for j in range(1, i+1):
        print("*", end=" ")
    for s in range(1, (5-i)*2+1):
        print(" ", end=" ")
    for j in range(1, i+1):
        print("*", end=" ")
    print()



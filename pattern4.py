n = int(input())
m = n+1
for i in range(1,n+1):
    for k in range(1,i):
        print(" ", end=" ")
    for j in range(i,n+1):
        print("*", end=" ")
    print()
    
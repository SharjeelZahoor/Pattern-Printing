n = 5
for i in range(1, n+1):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(1, i+1):
        print(i, end=" ")
    for j in range(1, i):
        print(i, end=" ")
    print()

for i in range(1, n):
    for j in range(1, i+1):
        print(" ", end=" ")
    for j in range(i, n):
        print(n+i, end=" ")
    for j in range(i, n-1):
        print(n+i, end=" ")
    print()



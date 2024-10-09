n = int(input("give your input :"))
for i in range(n):
    for j in range(n):
        if i == j or j+i == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
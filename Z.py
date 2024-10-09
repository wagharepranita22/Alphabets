n = int(input("give your input :"))
for i in range(n):
    for j in range(i,n):
        if i==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range (i):
        if i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()
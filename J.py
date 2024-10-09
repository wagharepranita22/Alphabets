n = int (input(" Enter your n th  value :"))
for i in range (n):
    for j in range(n):
        if (i==0 or j == n//2) or((i == n-1) and (j <= n//2)):
            print("*",end =" ")
        else:
            print(" ",end=" ")
    print()
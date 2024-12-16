r=int(input("enter a number:"))
for i in range(r):
    for j in range(r-i):
        print(" ",end="")
    for k in range(i+1,0,-1):
        print(k,end="")
    for k in range(2,i+2):
        print(k,end="")
    print()
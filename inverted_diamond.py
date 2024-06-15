num=int(input("Enter the number:"))
for i in range(0,num+1):
    for j in range(0,num-i-1):
        print("*",end=" ")
    print()

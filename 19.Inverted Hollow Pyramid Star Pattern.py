for i in range(1,5):
    for j in range(1,8):
        if i==1 or i+j==8 or j-i==0:
            print("*",end="")
        else:
            print(end=" ")
    print()

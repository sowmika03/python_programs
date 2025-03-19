n=6
for i in range(4):
    if i==0 or i==3:
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")

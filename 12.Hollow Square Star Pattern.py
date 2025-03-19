n=4
for i in range(n):
    if i==0 or i==3:
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")

password=input ()
l=len(password)
schar=(['!','@','#','$','%','^','&','*','/','?'," "])
if l<8:
    print("invalid password")
else:
    digit=False
    upper=False
    lower=False
    special_char=False
    for i in password:
        if i.isupper():
            upper=True
        elif i.islower():
            lower=True
        elif i.isdigit():
            digit=True
        elif i in schar:
            special_char=True
    if digit and upper and lower and special_char:
        print("valid password")
    else:
        print("invalid password ")

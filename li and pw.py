a="challamounikapriya7"
b="hi@"
for i in range(4):
    li=input('enter a login id')
    pw=input('enter a password')
    if li==a and pw==b:
        print("logged in successfully")
        break
    else:
        print("wrong credentials")
else:
    print("blocked for 24 hours")
    

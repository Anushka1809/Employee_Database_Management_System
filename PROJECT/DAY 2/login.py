import sys
print("Welcome to Employee System")
id=input("Please Enter Login id:  ")
pwd=input("Please Enter Password:  ")
file=open('login.txt','r')
a=file.readlines()
for i in a:
    b=i.split()
    if id==b[0] and pwd==b[1]:
        if id=='admin':
            import admin
            break
else:
    print("Invalid Login id and Password")
    sys.exit()
          
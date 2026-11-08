print("Enter element of first dictionary:")
mydict1={}
while True:
    key=input("Enter a key(or'q' to quit):")
    if key=='q':
        break
    value=int(input("Enter the value:"))
    mydict1[key]=value
print("enter element of sencond dictionary:")
mydict2={}
while True:
    key=input("Enter a key(or'q' to quit):")
    if key=='q':
        break
    value=int(input("Enter the value:"))
    mydict2[key]=value
print(mydict1|mydict2)

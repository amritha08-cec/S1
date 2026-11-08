import operator
mydict={}
while True:
    key=input("Enter a key(or'q'to quit):")
    if key=='q':
        break
    value=int(input("enter a value:"))
    mydict[key]=value
print("originaldictionary:",mydict)
sd=dict(sorted(mydict.items(),key=operator.itemgetter(1)))
print("Dictionary in ascending order:",sd)
sd=dict(sorted(mydict.items(),key=operator.itemgetter(1),reverse=True))
print("Dictionary in desendency order:",sd)

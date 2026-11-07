w=input("Enter the word:")
print("ordinal value of",w,"are:")
for x in dict.fromkeys(w):
    print(x,":",ord(x))

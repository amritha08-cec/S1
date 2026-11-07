n=(input("Enter the list of names:")).split(",")
count=0
print("list:",n)
for name in n:
    for i in name:
        if i[0]=='a' or i[0]=='A':
            count += 1
print("Number of a:",count)

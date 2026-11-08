clrs=[]
count=int(input("Enter the number of colors:"))
print("Enter the colors:")
for x in range(count):
    color=input()
    clrs.append(color)
print("firstcolor:",clrs[0],"| last color:",clrs[count-1])

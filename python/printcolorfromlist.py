list1=set()
list2=set()
n1=int(input("Enter the number of colors in list1:"))
print("Enter the color to list1:")
for x in range(n1):
    color=input()
    list1.add(color)
n2=int(input("Enter the number of colors in list2:"))
print("Enter the color to list2:")
for x in range(n2):
    color=input()
    list2.add(color)
diff=list1.difference(list2)
print("color in list 1 not in list 2:",diff)

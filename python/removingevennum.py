c = int(input("Number of elements: "))

l1 = []

for i in range(c):
    l1.append(int(input("Enter the element: ")))

for i in l1.copy():
    if i % 2 == 0:
        l1.remove(i)

print(l1)

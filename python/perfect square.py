result=[]
start=int(input("Enter the starting range(for-digit number):"))
end=int(input("Enter the ending range(for-digit number):"))
if start<1000 or end>9999 or start>end:
    print("invalid range.please enter a valid four-digit range.")
else:
        for num in range(start,end+1):
            if num%2==0:
                root=int(num**0.5)# taking the square root
                if root*root==num:#checking if it is a perfect square
                   result.append(num)#adding it to the list
print("four-digit even perfect square number in the given range:")
print(result)

s=input("Enter the string:")
first=s[0]
mod_str=first+s[1:].replace(first,'$')
print("modified string:",mod_str)

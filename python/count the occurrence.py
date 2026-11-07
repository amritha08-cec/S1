sentence=input("Enter the sentence:")
w=sentence.split()
counts={}

for word in w:
    if word in counts:
        counts[word]+=1
    else:
         counts[word]=1
print(counts)

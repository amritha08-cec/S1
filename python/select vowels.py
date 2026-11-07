w=input("Enter the word:")
vowels=['a','e','i','o','u','A','E','I','O','U']
word_vowels=[]
for x in w:
    if (x in vowels and x not in word_vowels):
        word_vowels.append(x)
print("vowels in",w,"are:",word_vowels)

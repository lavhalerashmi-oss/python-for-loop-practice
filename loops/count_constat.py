count the constant
text= input("Enter a word: ").lower()
count=0
for i in text:
    if i.isalpha() and i not in "aeiou":
        count +=1
print(count)    

#if i want to calculate only alphabets
text= input("Enter a word: ")
count=0
for i in text:
    if i.isalpha():
         count +=1
         print(i , end=" ")
print(count)    

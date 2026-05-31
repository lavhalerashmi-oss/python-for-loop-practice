word= input("Enter a word: ")
count=0
for i in word.lower():
     if i in "aeiou":
         count+=1
         print(i)
 print(count, "vowels")    

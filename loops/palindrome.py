word=input("Enter a word: ")  
for i in word:
    if word == word[::-1]:
        print(word, "This is palindrome")    
    else:
        print("not palindrome")    

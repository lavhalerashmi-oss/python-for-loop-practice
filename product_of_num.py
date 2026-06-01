# calculate the product of digits of number
num= input("Enter a number: ")
product=1
for i in num:
    product *= int(i)
print(product)    

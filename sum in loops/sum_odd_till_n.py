# sum of odd number
num= int(input("Enter a range for odd numbers:"))
sum= 0
for i in range(1, num + 1, 2):
    sum +=  i
print(sum ,"this is sum of odd number")

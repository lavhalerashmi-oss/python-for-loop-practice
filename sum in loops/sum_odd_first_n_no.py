#printing first  n odd number sum
num = int(input("Enter a number: "))
sum= 0 
for i in range(1, num+1):
    sum += 2*i-1
print(sum)

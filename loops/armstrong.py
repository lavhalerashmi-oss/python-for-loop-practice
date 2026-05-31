# printing armstrong number usign for loop
n = int(input("Enter a number: "))
sum= 0
digits= len(str(n))
for i in str(n):
    sum = sum + int(i) ** digits
print(sum)    
if n ==sum:
    print(f"yes {n} number is armstrong number")
else:
    print(f"no {n} is not armstrong number ")


# using while loop

n = int(input("Enter a number: "))
original = n 
sum= 0
digits= len(str(n))

while n>0:
    digit= n %10
    sum= sum+ digit ** digits
    n= n // 10
print(sum)

if original ==sum:
    print(f"yes {original} number is armstrong number")
else:
    print(f"no {original} is not armstrong number ")


 

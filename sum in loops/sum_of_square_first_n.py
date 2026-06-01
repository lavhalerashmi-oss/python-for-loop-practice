n= int(input("Enter a num: "))
sum= 0
for i in range(1, n+1 ):
    even = 2*i
    square= even*even
    sum +=  square
print(sum)

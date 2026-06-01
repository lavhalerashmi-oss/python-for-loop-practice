# find second largest number
l1.sort()
print(l1[-2])

l1 = [45, 78, 6, 49, 9, 23]

largest = l1[0]
second_largest = l1[0]

for i in l1:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print("Second largest:", second_largest)


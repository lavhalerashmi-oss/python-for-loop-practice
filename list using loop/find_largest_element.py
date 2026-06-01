# find largest element in list.
my_list=[ 45,56,67,90,78]
largest= my_list[0]
for i in my_list:
    if i > largest:
        largest= i
print("Greater number: ",   largest)
print(max(my_list)) 
 

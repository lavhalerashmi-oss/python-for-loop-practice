#find duplicate value
l1=[4,5,4,6,7,5,7]
dupli= {}
for i in l1:
    if i not in dupli:
        dupli[i]=1
    else:
        dupli[i] +=1  
print(dupli)       

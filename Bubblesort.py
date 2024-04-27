# take 2 elements and swap
l1=[64,34,25,12,22,11,90]
for i in range(len(l1)): # 0 1 2 3 4 5 6
    for j in range(i+1,len(l1)): # 1 2 3 4 5 6
        if l1[i]>l1[j]:
            temp=l1[j]
            l1[j]=l1[i]
            l1[i]=temp
print(l1)        

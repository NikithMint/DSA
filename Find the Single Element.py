arr=[8,8,9,9,10]
hash=[]
a=max(arr)
for i in range(a+1):
    hash.append(0)
  
for j in arr:
    
    hash[j]=hash[j]+1
for k in range(len(hash)):
    if hash[k]==1:
        print(k)
               
array=[] # 1 4 2 3 12 # tell how many times these appears
a=int(input())
for i in range(a):
    b=int(input())
    array.append(b)
print(array)
pre=[] # 1 3 2 1 3
d=int(input())
for k in range(d):
    e=int(input())
    pre.append(e)
print(pre)    
c=13
hash=[]
for l in range(c):
    hash.append(0)
print(hash)    
for n in pre:
    if n in array:    
        hash[n]=hash[n]+1
print(hash)

for g in array:
    print(hash[g])





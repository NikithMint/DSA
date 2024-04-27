a=int(input())
b=int(input())
l1=[]
l2=[]
l3=[]
for i in range(1,a+1):
    if a%i==0:
        l1.append(i)
for j in range(1,b+1):
    if b%j==0:
        l2.append(j)
                
for k in l1:
    if k in l2:
        l3.append(k)
print("HCF",max(l3))
print("LCM",min(l3))
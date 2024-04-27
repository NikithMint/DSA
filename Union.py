a=[1,2,3,3]
b=[5,2,10,2,4]
c=[]
for i in a:
    if i not in c:
        c.append(i)

for j in b:
    if j not in c:
        c.append(j)
c.sort()
print(c)      

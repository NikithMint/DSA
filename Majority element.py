from collections import Counter
x=[6,5,5]
y=Counter(x)
l1=[]
l2=[]
for i in y.keys():
    l1.append(i)
for j in y.values():
    l2.append(j)    
print(l1)
print(l2)
result=dict(zip(l1,l2))
maxx=max(zip(result.values(),result.keys()))[1]
print(maxx)
            
           
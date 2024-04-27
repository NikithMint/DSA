a=[3,4,5,1,2]
c=sorted(a)
count=0
for i in range(len(a)):
    b=a[i:]+a[:i]
    if b==c:
        count=count+1
    print(b)        
if count>=1:
    print("True")    

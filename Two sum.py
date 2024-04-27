a=[3,3]
target=int(input())
for i in range(len(a)):
    for j in range(i):
        b=a[i]+a[j]
        if b==target and i!=j :
            print(i,j)





            
            
            

nums=[9,6,4,2,3,5,7,0,1]
a=len(nums)
sum=0
b=int(a*(a+1)/2)
for j in nums:
    sum=sum+j  
c=b-sum
print(c)
        
nums=[1,2,3,4,5,6,7]
k=3
b=k
a=len(nums)-b

for i in range(len(nums)-b+1):
    if a==i:
        print(nums[i:]+nums[:i])
    
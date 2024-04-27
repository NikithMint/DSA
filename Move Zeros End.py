# with sorting
# nums=[0,0,0,1]
# nums.sort()
# print(nums)
# count=0
# for i in nums:
#     if i==0:
#         count=count+1
# print(nums[count:]+nums[:count])

# without sorting
nums=[0,1,0,3,12]
l1=[]
count=0
for i in nums:
    if i==0:
        count=count+1
    else:
        l1.append(i)
for j in range(count):
    l1.append(0)        
print(l1)
def sort(nums):
    for i in range(5):
        minpos=i
        for j in range(i,6):
            if nums[j]<nums[minpos]:
                minpos=j
                
        temp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp
print(sort([5,2,3,8,6,7]))

# selection sort
# find the min value

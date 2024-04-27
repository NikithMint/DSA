from collections import Counter


a=[0,0,1,1,1,2,2,3,3,4]
b=Counter(a)

# for i in b.keys():
#     print(i)
print(list(b.keys()))
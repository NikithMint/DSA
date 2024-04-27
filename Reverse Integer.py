a=[1,2,3,4]
print(a[::-1])
print(a[:-1])
if a[0]=="-":
    print(f"{a[0]}{a[:-1]}")
else:
    print(a[:-1])    
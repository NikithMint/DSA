def facto(x):
    if x==1:
        return x
    else:
        return x*facto(x-1)
print(facto(5))

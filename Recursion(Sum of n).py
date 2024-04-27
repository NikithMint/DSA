def sumofn(x):
    if x<=1:
        return x
    else:
        return x + sumofn(x-1)
            
print(sumofn(5))    


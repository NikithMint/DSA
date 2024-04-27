def ntimes(x):
    if x>0:
        ntimes(x-1)
        print("HELLO",end=" ")
ntimes(3)
    
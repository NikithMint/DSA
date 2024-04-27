def oneton(x):
    if x>0:
        oneton(x-1)
        print(x,end=" ")
oneton(10)
        
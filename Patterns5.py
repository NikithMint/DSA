a=int(input())
for i in range(a):
    for j in range(a-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    for l in range(a-i-1):
        print(" ",end="")
    print()

# output 
#      *
#     ***
#    *****
#   *******
#  *********
# ***********    

    

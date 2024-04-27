a=int(input())

for i in range(a):
    print("*",end="")
print()
for m in range(a-2):
    for j in range(2): 
        print("*",end="")
        for l in range(a-2): 
            print(" ",end="")
    print()
for n in range(a):
    print("*",end="")

    
# output 
# *****
# *   *
# *   *
# *   *
# *****    
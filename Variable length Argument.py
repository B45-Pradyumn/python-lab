# VARIABLE LENGTH ARGUMENTS
def add(*a):
    s=0
    for i in a:
        s=s+i
    print(s)
add(1,3)
add(100)
add(1,2,3)
add(1,2,3,4,5,6,77,8,9,9)


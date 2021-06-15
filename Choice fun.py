# RANDOM.CHOICE FUNCTION
import random
m=1,2,3,4,5,6,7
l=["Red","Blue","Yello","Pink","Green","White","Black","Orange","Silver"]
print(random.choice(l))
print(random.choices(l))

print(random.choice(m))
print(random.choices(m))

print(random.choices(l,k=3)) # Any 3 colours will be shown 
print(random.choices(m,k=3)) # Any 3 numbers will be shown

print(random.choices(l,weights=[15,10,3,6,8,4,30,7,25],k=4)) # weight gives the possibility
print(random.choices(m,weights=[15,10,3,6,8,4,7],k=10))

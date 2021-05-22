s1={100,200, 300, 400, 500}
s2={400, 500, 600, 700, 800,900}
#function
print(s1.symmetric_difference(s2))
#Symbol
print((s1-s2).union(s2-s1))

### OR

#function
print(s2.symmetric_difference(s1))
#Symbol
print(s2^s1)

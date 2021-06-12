# GLOBAL VARIABLE

a=5       #global
def fun():
    global a 
    a=a+10  #local(XXXXXxxx)
    print("Inside the functon",a)
fun()
print("Outside the function",a)
    
    

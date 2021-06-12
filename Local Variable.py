# LOCAL VARIABLE

a=5       #global
def fun():
    b=6
    a=100 #local
    a+=1  
    print("Inside the functon",a)
fun()
print("Outside the function",a)
    
    

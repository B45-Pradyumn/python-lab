# REVERSE OF A NUMBER
num=int(input( "Enter a number:"))
n=0
while (num>0):
        rem=num%10
        n=(n*10)+rem
        num=num//10
print("the reverse number is :{}".format(n))
        
        

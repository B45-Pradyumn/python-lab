def is_power_of_2(n):
    if n<=0:
        return False
    else:
        return n &(n-1)==0
n=int(input('Entera no.:'))
if is_power_of2(n):
    print('{}is a power of 2'.format(n))
else:
    print('{} is not a power of 2.'.format(n))
    

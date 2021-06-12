#FUNCTION IN FUNCTION

a=5
def fun1():
    b=10
    def fun2():
        c=20
        print(c)
        print(c,b,a)
    print(b,a)
    print(b)
    fun2()
fun1()
print(a)

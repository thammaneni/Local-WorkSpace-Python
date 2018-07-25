def fun1():
    print("This is normal function")

def fun2(arg1,arg2):
    print("arg1 : ",arg1," arg2 :",arg2)

def fun3(x,*args):
    result =0;
    for i in args:
        result = result + i;
    x=result *x;
    return x
    
fun1()
fun2(10,15)
fun2(arg2=15,arg1=10)
print(fun3(5,1,1,1,1,1,1))



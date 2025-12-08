def deco(fun):
    def inner():
        result=fun()
        n3=eval(input("num3:"))
        return result+n3
    return inner 

@deco 
def add():
    n1=eval(input("num1:"))
    n2=eval(input("num2:"))
    
    
    
def uppercase(fun):
    def inner(f,l):
        fname=fun(f,l)
        return fname.upper()
    return inner
@uppercase
def fullname(fn,ln):
    return f'{fn}{ln}'
     
print(fullname('suraj' ,'singh'))     

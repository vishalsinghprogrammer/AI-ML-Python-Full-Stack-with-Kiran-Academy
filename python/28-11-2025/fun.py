""" 
def square():
    num=eval(input("enter number="))
    square=num**2
    print(square)
square() """
#create a function to check num is even or not
 
'''def EvenOdd():
    num=eval(input("enter number="))
    if num%2==0:
        print("number is even")
    else:
        print("number is odd")
EvenOdd() '''
#positive or negative or zero
""" 
def posNeg():
    num=eval(input("enter number="))
    if num>0:
        print("number is positive")
    elif num<0:
        print("number is negative")
    else:
        print("number is zero")
posNeg() """
# create to check one number is devisible by second
""" 
def div():
    num1=eval(input("enter 1st number="))
    num2=eval(input("enter 2nd number="))
    if num1%num2==0:
        print(f"print {num1} is divisible by {num2}")
    else:
        print(f"print {num1} is not divisible by {num2}")
div()
"""
#create a function to count length of any iterable
""" 
def length():
    str=input("enter string=")
    count=0
    for ch in str:
        count+=1
    print(f"count={count}")
length()
"""
"""
def length():
    str=input("enter string=")
    ch=input("enter string=")
    count=0
    for i in str:
        if ch==i:
            count+=1
    print(f"count={count}")
length() """

""" 
def length():
    str=input("enter string=")
    l=["a","e","i","o","u"]
    count=0
    for i in str:
        for j in l:
            if i==j:
                count+=1
    print(f"count={count}")
length()
"""
#parameter and argument
"""
def add(n1,n2):#
    sum=n1+n2
    print(sum)
num1=eval(input("enter 1st number="))
num2=eval(input("enter 2nd number="))
add(num1,num2) """
#create a function to count number of character in the string
"""
def countel(string):
    count=0
    for char in string:
        count+=1
    print(count)

str=input("enter string=")

countel(str)"""
#create a function to chech number of perticular char in string
"""
def countChar(string,char):
    count=0
    for c in string:
        if c==char:
            count+=1
    print(count)

str=input("enter string=")
ch=input("enter character=")
countChar(str,ch)
"""
#create a function to chech space of perticular char in string
""" 
def countspace(string):
    count=0
    p=" "
    for c in string:
        if p==c:
            count+=1
    print(count)

str=input("enter line=")
countspace(str)
"""
#create a function reverse the string
"""
def reverse(string):
    value=""
    for c in string:
        value=c+value
    print(value)

name=input("enter string=")
reverse(name)
"""
"""
#types or argument
   1.positional argument:maintain position of argument
   2.keyword argument:value(argument) passed by specifying parameter name(eg:fun(p2=v2,p1=v1)),no need to maintain position
   3.default argument:set default value to parameter(eg:def fun(p1,p2=v)),if we set parameter value default then need to write all default value to all parameter after that 
   4.arbitary argument:
       a.positional arbitary argument
       b.keyword arbitary argument
   note:-1st positional then keyword argument
"""
"""
def fullName(fn,mn,ln):
    fullname=f"{fn} {mn} {ln}".title()
    print(fullname)

fullName("gauri","suresh","bhoj")#positional argument(Gauri Suresh Bhoj)
fullName("bhoj","gauri","suresh")#positional argument(Bhoj Gauri Suresh)

fullName(ln="bhoj",fn="gauri",mn="suresh")#keyword argument(Gauri Suresh Bhoj)
"""
def student(name,course,institute):
    stdinfo=f'''
    Name:{name},
    Course:{course}
    Institute:{institute}
    '''
    print(stdinfo)

student("eevee","wd","rk institute")
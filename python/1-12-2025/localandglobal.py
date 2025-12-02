def sum(n1,n2):
    result=n1+n2
    return result 

print(sum(10,20))
ans=sum(4,5)
print(ans**2)



def calci(n1,n2):
    sum=n1+n2
    sub=n1-n2
    mul=n1*n2
    div=n1/n2
    return sum,sub,mul,div

print(calci(10,2))
t=calci(10,5)
print(t)


sum,sub,mul,div=calci(10,3)
print(sum)    
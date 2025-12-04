#create a function to check number is prime or not ?

# def isprime(num):
#     for i in range(2,num):
#         if num%i==0:
#           return True
#     return False
# print(isprime(7))    


#create a function to check number is perfect or not ?

def isperfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum=i
    if sum==num:
        return True
    else:
        return False
print(isperfect(6))    
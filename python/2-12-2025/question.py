
#create a function to check prime or not ?
# def isprime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
# print(isprime(5))    


#create a function to check perfect or not ?


# def isperfect(num):
#     sum=0
#     for i in range(1,num):
#         if num%i==0:
#            sum=sum=i
#     if sum== num :
#         return True
#     else:
#         return False      
      
      
      
      
# print(isperfect(6))
      #create a function to check Armstrong or not ?
      
# def isarmstong(num):
#     snum=str(num)
#     no=len(snum)
#     sum=0
#     for i in snum:
#         sum=sum+int(i)**no
#     if sum==num:
#         return True
#     else:
#         return False      
    
    
# print(isarmstong(153))    
      
      
#fuction => iterable of numbers => return iterable of only prime numbers

# def isprime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
# def filter_prime(iterble):
#     prime_numbers=[] 
#     for num in iterble:
#         if isprime(num):
#             prime_numbers.append(num)
#     return prime_numbers
# print (filter_prime([1,5,6,7,21,55]))  


#2 method
# def filter_prime(iterable):
#     prime_numbers=[]
#     for num in iterable:
#         for i in range(2,num):
#             if num%i==0:
#               break
#         else:
#             prime_numbers.append(num)
#             return prime_numbers
# print(filter_prime([1,5,6,7,21,55]))        
               
   
      
   #fuction => iterable of numbers => return iterable of only perfect numbers    
def filter_perfect(iterable):
    perfect_number=[]
    sum=0
    for num in iterable:
        for i in range(1,num):
            if num%i==0:
                sum+=i
        if sum==num:
            perfect_number.append(num)
        else:
            sum=0
    return perfect_number
print(filter_perfect([3,5,6,8,9,12,28,]))
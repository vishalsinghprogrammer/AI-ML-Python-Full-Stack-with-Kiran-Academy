# # #1)write a program to take a user range number and calculate the sum of its even and odd number return list for odd and even number and return total_no of even odd also return list for total_even_number_list and total_odd_number_list

# # start = int(input("Enter starting number: "))
# # end = int(input("Enter ending number: "))

# # even_list = []
# # odd_list = []

# # for num in range(start, end + 1):
# #     if num % 2 == 0:
# #         even_list.append(num)
# #     else:
# #         odd_list.append(num)

# # print("Even number list:", even_list)
# # print("Odd number list:", odd_list)

# # print("Total even numbers:", len(even_list))
# # print("Total odd numbers:", len(odd_list)) 
 
# # #Write a program to check if a given string is a palindrome or not using loops?
# # s = input("Enter a string: ")
# # rev = ""

# # for ch in s:
# #     rev = ch + rev   # build reverse string using loop

# # if s == rev:
# #     print("The string is a Palindrome")
# # else:
# #     print("The string is NOT a Palindrome")
    
# #3. Write a program to check if a given string is a palindrome or using loops.

# # s = input("Enter a string: ")
# # rev = ""

# # for i in s:
# #     rev = i + rev   
# # if s == rev:
# #     print("Palindrome")
# # else:
# #     print("Not a Palindrome")
    
# #4. Write a program to find the frequency of each character in a string (how many each character occurs) print a dict

# # s = input("Enter a string: ")
# # freq = {}

# # for ch in s:
# #     if ch in freq:
# #         freq[ch] += 1
# #     else:
# #         freq[ch] = 1

# # print("Character frequency:", freq)

# #5 Write a program to to check whether a given number is Prime or not.
# num = int(input("Enter a number: "))

# if num <= 1:
#     print("Not a Prime Number")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a Prime Number")
#             break
#     else:
#         print("Prime Number")


# #write a program to check  whether a number is strong number or not  #(strong number = sum of factorial digits =number)
    
# num = int(input("Enter a number: "))
# temp = num
# sum_fact = 0

# while temp > 0:
#     digit = temp % 10
#     fact = 1

#     for i in range(1, digit + 1):
#         fact = fact * i

#     sum_fact = sum_fact + fact
#     temp = temp // 10

# if sum_fact == num:
#     print(num, "is a Strong Number")
# else:
#     print(num, "is not a Strong Number")
    
# #15) write a program  to check whether a  give number is strong number or not
# #Example : 121-> palindrome , 123-> not palindrome
# #16) write a program to check the number is "Buzz Number" or not
# # = number which is divisible by 7
# # = and 7 should not present in number as digit
# # e.g
# # a=49
# def pro15():
#     a=int(input("enter number"))
#     if a%7==0 and
 
 
#  #write a program to add only Armstrong number into list  
  
# list=[1,10,50,78,72,82] 
# for i in list:
#     print(i)


# students=[]
# while cont=='yes':
    
#what is DAT-type?
#what is looping satement
#diff between for-loop and whileloop
#what is purpose of conditional statement
#what is purpose of continue and break    
    
#Write a program to check if a given string is a palindrome or not using loops?
# word = input("Enter a Word: ")
# rev = ""

# for char in word:
#     rev = char + rev   

# if word  == rev:
#     print("Palindrome")
# else:
#     print(" NOT a Palindrome")

#write a program to find the frequency of each character in a string (how many times each character occors)

# s =input("Enter a sting")
# freq={}
# for char in s:
#     if char not in freq:
#         freq[char]+1
#     else:
#         freq[char]=freq[char]+1
# print(freq)             
    
# creat a function to calculte  addion a two number
# def add_number(n1,n2):
#     add = n1+n2
#     return add 
# r=add_number(10,7)
# print(r)

# def sum (n1=0,n2=0):
#     result=int(n1)+int(n2)
#     return result 
# print(sum())


# def sum(n1=0,n2=0):
#     if isinstance(n1,)

#write a function to return power of number
# eg base , power=5 ;

# write a function to return count of number which is divisinbble by 4(range-123 to 233)


#write a function to check the number is prime number or not 

# def checkprimenumber(num):
#    count =0
#    for i in range(1,num+1):
#        if (num%i==0):
#            count+=1
#    if(count==2):
#         print("prime number")
#    else:
#        print("not prime number")       
           
    
#write a function to print prime number from 1 to 100
# def checkprimenumber(num):
#    count =0
#    for i in range(1,num+1):
#        if (num%i==0):
#            count+=1
#    if(count==2):
#         print("prime number")
#    else:
#        print("not prime number") 
# for num in range(1,101):
#      checkprimenumber()


# write a function to print count of print number from 1 to 100

# def count_primenumber():
#     count_prime = 0
    
#     for num in range(2, 101):
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             count_prime += 1
            
#     print("Total Prime Numbers:", count_prime)

# count_primenumber()

# write a function to print divisor of number e.g 12=1,2,3,4,6,12
# def divisor(n):
#     for i in range(1, n+1):
#         if n % i == 0:
#             print(i)

# divisor(12)


#write a function to return count of divisor of number
# def count_divisor(n):
#     count = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             count += 1
#     return count

# print(count_divisor(4))

#write a function to orint sum os divisor of number

#write a function to check the number is perfect number or not #e.g n=28=1,2,4,7,14,28 sum=1+2+4+7+14+
#write a function to print perfect number from 1 to100

# def perfect():
#     for n in range(1, 101):
#         s = 0
#         for i in range(1, n):
#             if n % i == 0:
#                 s += i
#         if s == n:
#             print(n)

# perfect()



# create a function  to check  prime  number or not.
# num = int(input("enter num:"))
# for i in range (2,num):
#     if num%1 ==0:
#         print("Not Prime")
#         break
# else:
#     print("prime")    
    
    
#write a program to print a list of prime number for 1 to 500
# prime=[]
# for num in range(2,501):
#     for i in range(2,num):
        
#         if num%i==0:
#             break
#     else:
#             prime.append(num)
# print(prime)

# #
# def prime():
#     for num in range (2,501):
#         for i in range (2,num):
#             if num %i==0:
#                 break
#         else:
  # write a program to check whether given number is armstrong number   or not       
# num =int(input("number"))
# snum=str(num)
# n=len(sum)
# sum=0
# for i in snum:
#     sum=sum+int(i)**n
# if num ==sum :
#     print(True)
# else:
#     print(False)   

#wrp list of armstrong from given range



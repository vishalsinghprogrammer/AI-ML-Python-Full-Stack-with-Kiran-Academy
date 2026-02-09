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
    

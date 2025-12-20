# #1)write a program to take a user range number and calculate the sum of its even and odd number return list for odd and even number and return total_no of even odd also return list for total_even_number_list and total_odd_number_list

# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))

# even_list = []
# odd_list = []

# for num in range(start, end + 1):
#     if num % 2 == 0:
#         even_list.append(num)
#     else:
#         odd_list.append(num)

# print("Even number list:", even_list)
# print("Odd number list:", odd_list)

# print("Total even numbers:", len(even_list))
# print("Total odd numbers:", len(odd_list)) 
 
# #Write a program to check if a given string is a palindrome or not using loops?
# s = input("Enter a string: ")
# rev = ""

# for ch in s:
#     rev = ch + rev   # build reverse string using loop

# if s == rev:
#     print("The string is a Palindrome")
# else:
#     print("The string is NOT a Palindrome")
    
#3. Write a program to check if a given string is a palindrome or using loops.

# s = input("Enter a string: ")
# rev = ""

# for i in s:
#     rev = i + rev   
# if s == rev:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")
    
#4. Write a program to find the frequency of each character in a string (how many each character occurs) print a dict

# s = input("Enter a string: ")
# freq = {}

# for ch in s:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1

# print("Character frequency:", freq)

#5 Write a program to to check whether a given number is Prime or not.
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prime Number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")


    
    
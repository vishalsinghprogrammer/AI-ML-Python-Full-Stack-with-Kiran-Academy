# # str=input("enter string:")
# # print(type(str))

# # l=input("enter string")
# # print(len(l))

# #wap to check lenght of given sting if length is more than 8 than its valid string otherwise its invalid .

# l=input('enter string:')
# if len(l) >=8:
#     print('Its valid string')
# else:
#     print('Invalid String')
    
# #wap to check lenght of given sting 
# # if length is more than 8 than its valid string otherwise its invalid .
# # if that string contains white space " " then also that string invalid.

# l=input('enter string:')
# if len(l) >=8 and " " not in l:
#     print('Its valid string')
# else:
#     print('invalid string')
    
# #wap to check lenght of given sting 
# # if length is more than 8 than its valid string otherwise its invalid .
# # if that string contains white space " " then also that string invalid.
# # if that string not contains digit/number still it is invalid.
# l=input('enter string:')
# if len(l) >=8 and " " not in  l and any(ch.isdigit() for ch in l):
#     print('Its valid string')
# else:
#     print('Invalid string') 
    
    
# #wap to check lenght of given sting 
# # if length is more than 8 than its valid string otherwise its invalid .
# # if that string contains white space " " then also that string invalid.
# # if that string not contains digit/number still it is invalid.
# #at least one capital must be present in your string .    




    
# #wap to check lenght of given sting 
# # if length is more than 8 than its valid string otherwise its invalid .
# # if that string contains white space " " then also that string invalid.
# # if that string not contains digit/number still it is invalid.
# #at least one capital must be present in your string . 
# # at least contains one special symbol !@#$%^&*~



# def Pass_validation(password):
#     if len(password)<8:
#         return f"You pass word len is {len(password)}and required is greater than 7"
#     if " " in password:
#         return "Remove white spaces in your password"
#     if not any (ch.isdigit()for ch in var):
#         return "Add atlearst 1 digit in your password"
#     if not any (ch.upper()for ch in var):
#         return "NO upper case letter"
#     if not any (ch.lower()for ch in var):
#         return "NO lower case letter" 
#     if not any (ch.specil in "~!@#$%^&*" for ch in var):
#         return "NO special symbol present" 
#     return "Password valid"
    
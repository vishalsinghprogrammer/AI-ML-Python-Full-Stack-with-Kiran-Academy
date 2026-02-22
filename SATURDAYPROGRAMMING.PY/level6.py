
# c_unit = {
#     "harish": 140,
#     "kiran": 120,
#     "mayur": 40,
#     "om": 160,
#     "rahul": 399,
#     "omkar": 400,
#     "pavan": 500,
#     "vijay": 250
# }

# bill = {}

# for name, unit in c_unit.items():
    
#     if unit < 100:
#         amount = unit * 5
#     elif 100 <= unit <= 200:
#         amount = unit * 10
#     elif 200 < unit <= 500:
#         amount = unit * 11
#     else:
#         amount = unit * 15
    
#     bill[name] = amount

# print(bill)


# for i in range (1,6):
#     for j in range(1,6):
#         print(j,end =" ")
#     print()
    
    
#print the re
# for j in range (3):
#     for i in range (4):
#         print("*",end=" ")
#     print()    
    
#print the rectangle of 10 by 5    
# for i in range(5):          
#     for j in range(10):    
#         print("*", end=" ")
#     print()

#a=65
# print(a)
# b=(a)
# print(b)
# print(b)
# print()
# print(c)
# d=ord(c) 
# print(d)   #charavter to number

# for i in range(1,6):
#     a=65
#     for j in range (1,6):
#         print(chr(a),end="  ")
#         a=a+1
#     print()  

# char=(int(input("enter the chr")))
  
#5 4 3 2 1
# for i in range (5,0,-1):
#     for j in range(5,0,-1):
#         print(j,end=" ")
#     print()
    
    

# for i in range(6,1,-1):
#     a=65
#     for j in range (6,1,-1):
#         print(chr(a),end="  ")
#         a=a+1
#     print()      
    
# Print triangle pattern

rows = 4

for i in range(1, rows + 1):
    print(" * " * i)    
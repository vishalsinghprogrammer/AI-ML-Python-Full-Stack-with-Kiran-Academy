'''
Comprehensions in Python are concise and efficient constructs for creating new sequences (like lists, dictionaries, and sets) from existing iterables. They offer a more readable and often faster alternative to traditional loops for tasks involving data transformation and filtering.


'''
# 1.new_list=[exp for var in iterable]

# students=['vishal singh,''suraj singh','aman singh','prince singh']
# st=[name.tital{} for name in students]
# print(st)

# result={'vishal singh':20,'suraj singh':55,'aman singh':88,'prince singh':75}
# st=[name for name in result]
# print(st)

# cube=[num**3 for num in range(1,11)]
# print(cube)


# 2.new_list=[exp for var in iterable if cond]

# numbers=[1,5,4,9,8,7,8,6]
# square_even=[num**2 for num in numbers if num%2==0]
# print(square_even)

# students=['vishal singh,''suraj singh','saman singh','sprince singh']
# nm=[name for name in students if name.startswith('s')]
# print(nm)

# result={'suraj singh':55,'aman singh':34,'prince singh':98,'vishal singh':12}
# passed=[name for name in result if result[name]>=40 ]
# print(passed)

# 3.new_list=[exp if con else exp2 for var in iterable]

# numbers=[1,2,3,4,65,6,7,89,9]
# sc=[num**2 if num%2==0 else num**3 for num in numbers]
# print(sc)


# result={'suraj singh':55,'aman singh':34,'prince singh':98,'vishal singh':12}
# l=[name.upper() if result[name]>=40 else name.lower()for name in result]
# print(l)

# 1.new_list={k:v for var in iterable}

# numbers=[1,2,3,4,65,6,7,89,9]
# square={num:num**2 for num in numbers}
# print(square)

# numbers=[1,2,3,4,5,6]
# cube={num:num**3 for num in numbers if num%2==0}
# print(cube)


#2. new set = {k:v for var in iterable if cond} 


# product_mrp={'leptop':56000,'mbl':10000,'speaker':67000,'Tv':30000,'headphone':25000}
# product_25k={product:mrp for product,mrp in product_mrp.items() if mrp>25000}
# print(product_25k)


# product_mrp={'leptop':56000,'mbl':10000,'speaker':67000,'Tv':30000,'headphone':25000}
# product_sp={product:mrp-mrp*5/100 for product,mrp in product_mrp.items()if mrp>25000}
# print(product_sp)



#new_dict={k:v1 if condision else v2 for vr in itreable}


# numbers={1,2,3,4,5,67,8}
# sc={num:num**2 if num%2==0 else num**3 for num in numbers}
# print(sc)

# result={'suraj singh':55,'aman singh':34,'prince singh':98,'vishal singh':12}
# final={name:'pass'if mark>=40 else 'fail'for name,mark in result.items()}
# print(final)


# mbl_mrp={'cel':56000,'ce2':10000,'ce3':67000,'ce4':30000,'ce5':25000}
# price={model :model for model in mbl_mrp if mbl_mrp[model]>40000}
# print(price)


# numbers={1,4,5,6,7,3,2,9,8}
# n={num for num in numbers if num%2==0 }
# print(n)


# numbers=[1,2,3,4,5,6]
# square={num:num**2 for num in numbers}
# print(square)

# product_mrp={'leptop':56000,'mbl':10000,'speaker':67000,'Tv':30000,'headphone':25000}
# product_sp={product:mrp-mrp*10/100 for product,mrp in product_mrp.items()}
# print(product_sp)

# numbers=[1,2,3,4,5,6]
# cube={num:num**3 for num in numbers if num%2==0}
# print(cube)
'''
#list_new=[exp for in var iterable]
#list_new=[exp for in var con]
#list_new=[ex for in ]
'''
 
 
 
name1={'vishal':20,'suraj':18,'aman':25,'prince':5,'kamlesh':58}
all_name={name for name in name1}

print(all_name)

eligible={name for name,age in name1.items() if age>=18 }
print(eligible)
  
'''
  list comprehension 
  
1. new _list = [exp for var in iterable]
2. new list = [exp for var in iterable if cond] 
3.new list = [exp if cond else exp2 for var in iterable] 
set comprehension 

1. new_set = {exp for var in iterable}  
2. new set = {k:v for var in iterable if cond} 
3. new _dict = {k:v1 if cond else v2 for var in iterable}
   
   new_set = {k:v for var in iterable} 
   
'''
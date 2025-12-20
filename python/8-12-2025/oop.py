# class Student:
#     pass 



# s1=Student()
# s2=Student()
# print(type(s2))


class Students:
    def __init__(self):
        print(f'id of self:{id(self)}')
s1=Students               
print(f'id of s1:{id(s1)}')
print('-'*100)
s2=Students()
print(f'id of s2:{id(s2)}')
print('-'*100)
s3=Students()
print(f'id of s3:{id(s3)}')     

class Empoly:
    def __init__(self):
        print(f'id')   
        
        
'''
1.method :
     function =>class =>block of code =>operations=>data


1.instance method: 
   object level 
   first  perameter is self  
   we can call bye obj refrence
   self
   
2. class method 
   -class level 
   -first perameter is cls 
   -@classmethod 
   -obje ref or classname
   -self of classname
'''
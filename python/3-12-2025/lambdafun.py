# print((lambda n1,n2:n1+n2(1,3)))

# square=lambda num:num**2
# print(square(5))



#create a function to create full name

# fullname=lambda fn,mn,

#

# per=lambda obt,total:(obt/total)*100
# print(per(60,100)) 

#create a lambda function to calclute selling price 

# sellingprice=lambda mrp,dis:mrp-(mrp*dis/100)
# print(sellingprice(10000,19))





#Higher order function

# numbers=[10,20,33,55,46,88,25,78,]
# print(list(filter(lambda num:num%2==0,numbers)))


# numbers=[10,-20,33,-55,46,-88,25,78,]
# print(list(filter(lambda num:num>0,numbers)))

# student=['kunal','om','raj','kiran','atul','pradip','rajesh','bhushan','vaibhav','karan','vijay','varun']
# print(list(filter(lambda name:len(name)>5,student)))

 #print list of name of pass student 
# student={'kunal':89,'om':78,'raj':85,'kiran':79,'atul':45,'pradip':30,'rajesh':35,'bhushan':55,'vaibhav':25,'karan':56,'vijay':41,'varun':15}
# print(list(filter(lambda value : student[value]>=40,student)))

#print dic of passed student {'kunal:89'}
# student={'kunal':89,'om':78,'raj':85,'kiran':79,'atul':45,'pradip':30,'rajesh':35,'bhushan':55,'vaibhav':25,'karan':56,'vijay':41,'varun':15}
# print(dict(filter(lambda t:t[1]>=40,student.items())))


# student=['kunal','om','raj','kiran','atul','pradip','rajesh','bhushan','vaibhav','karan','vijay','varun']
# print(list(map(lambda name:name.upper(),student)))
# print(dict(map(lambda name:(name,len(name)),student)))


# number=[1,2,3,4,5,6,7,8,9]
# print(list(map(lambda num:num**2,number)))
# print(dict(map(lambda num:(num,num**2),number)))

# students=['vainhavpatil','rameh wagh','rajesh tope','suraj singh','prince prjapati','kunal kale']

#20k=>10%=>dict
product={'laptop':50000,'mobile':25000,'bag':10000,'fan':5000,'Tv':40000}
filter(lambda :product)
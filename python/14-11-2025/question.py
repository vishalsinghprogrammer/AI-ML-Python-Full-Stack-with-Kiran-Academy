result={'kunal':56,'karan':10,'ajay':78,'sujay':79,'varun':21}

result={'kunal':56,'karan':10,'ajay':78,'sujay':79,'varun':21}
for name,marks in result.items():
    if marks>=40:
       print(name)
       
       
result={'kunal':56,'karan':20,'ajay':78,'sujay':79,'varun':21}       
passed=[]
failed=[]
for name,marks in result.items():
 if marks>=40:
    passed.append(name)
 else:
    failed.append(name)   
print(f'passed student:{passed}')  
print(f'failed student:{failed}')    


result={'kunal':56,'karan':10,'ajay':78,'sujay':79,'varun':21} 
final_result={}
for name,marks in result.items():
 if marks >= 40:
    final_result[name] ='pass'
else:
     final_result[name] ='fail'
print(final_result)


#mble_sp={'model':sp}=>offer=> price50k
mbl_mrp={'ce1':56000,'ce2':10000,'ce3':67000,'sujay':30000,'varun':25000}




mbl_mrp={'cel':56000,'ce2':10000,'ce3':67000,'ce4':30000,'ce5':25000}
#object
mobile_sp={}
for mobile,price in mbl_mrp.items():
#56000 #67000
   if price>50000:
      dp=price*30/100 # 16800 # 20100
      sp=price-dp # 39200 #46900
      mobile_sp[mobile]=sp 
   else:
     #10000 #30000 #25000
      dp=price*15/100 # 1500 #4500 #3750
      sp=price-dp #8500 #25500 #21250
      mobile_sp[mobile]=sp 
print( mobile_sp) #{'cel':39200} #{'cel':39200, ce2:8500 } 
 


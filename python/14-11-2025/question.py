#result={'kunal':56,'karan':10,'ajay':78,'sujay':79,'varun':21}

# result={'kunal':56,'karan':10,'ajay':78,'sujay':79,'varun':21}
# for name,marks in result.items():
#     if marks>=40:
#        print(name)
       
       
# result={'kunal':56,'karan':20,'ajay':78,'sujay':79,'varun':21}       
# passed=[]
# failed=[]
# for name,marks in result.items():
#  if marks>=40:
#     passed.append(name)
#  else:
#     failed.append(name)   
# print(f'passed student:{passed}')  
# print(f'failed student:{failed}')    


result={'kunal':56,'karan':10,'ajay':78,'sujay':79,'varun':21} 
final_result={}
for name,marks in result.items():
 if marks >= 40:
    final_result[name] ='pass'
 else:
     final_result[name] ='fail'
print(final_result)


# #mble_sp={'model':sp}=>offer=> price50k
# mbl_mrp={'ce1':56000,'ce2':10000,'ce3':67000,'sujay':30000,'varun':25000}

# 50000< (30%) 
# 50000> (15%)

# mbl_mrp={'cel':56000,'ce2':10000,'ce3':67000,'ce4':30000,'ce5':25000}
# mobile_sp={}

# for mobile,price in mbl_mrp.items():
#     if price > 50000:
#         dp = (price/100) * 30
#         # print('dp:',dp)
#         sp = price - dp
#         print('sp:',sp)
#         mobile_sp[mobile] = sp
#     else:
#         dp = (price/100) * 15
#         # print('dp:',dp)
#         sp = price - dp
#         print('sp:',sp)
#         mobile_sp[mobile] = sp
# print(mobile_sp)       


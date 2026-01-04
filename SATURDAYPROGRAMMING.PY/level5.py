#creat a functional calculate factorial of any number by func
#create a fun calculate seling price of product od dicount
#

# def mrp_price(mrp,dis)
#     dp = mrp *dis/100

# def percentage(obt,total):
#     per=obt/total*100
 
# class Student:
#     def __init__(self,rll,nm):
#         self.roll=rll
#         self.name=nm
#         self.marks={}
#     def add_marks(self,**mks):
#         self.marks.update(mks)  
#         print(self.marks)
        
        
#     def obt_marks(self):
#         all_marks=list(self.marks.values()) 
#         obt=sum(all_marks)  
#         return obt
    
#     def percentage(self):
#         obt=self.obt_marks()
#         total=len(self.marks)*100
#         per=obt/total *100
#         return per
    
#     def get_result(self):
#         per=self.percentage()
#         if per>=40:
#             return 'Pass'
#         else:
#             return 'Fail'
        
#     def display (self):
        
        
#         pass 
    




# class Employee:
#     def __init__(self, emp_id, name, basic_salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.basic_salary = basic_salary

#     def calculate_allowances(self):
#         self.hra = self.basic_salary * 0.20   # 20% HRA
#         self.da = self.basic_salary * 0.10    # 10% DA

#     def calculate_gross_salary(self):
#         self.calculate_allowances()
#         self.gross_salary = self.basic_salary + self.hra + self.da

#     def calculate_net_salary(self):
#         self.calculate_gross_salary()
#         self.tax = self.gross_salary * 0.10  
#         self.net_salary = self.gross_salary - self.tax

#     def display_payslip(self):
#         self.calculate_net_salary()
#         print("------ Employee Pay Slip ------")
#         print("Employee ID   :", self.emp_id)
#         print("Employee Name :", self.name)
#         print("Basic Salary  :", self.basic_salary)
#         print("HRA (20%)     :", self.hra)
#         print("DA (10%)      :", self.da)
#         print("Gross Salary  :", self.gross_salary)
#         print("Tax (10%)     :", self.tax)
#         print("Net Salary    :", self.net_salary)
# emp = Employee(102,"Vishal",40000)
# emp.display_payslip()
      
    
class BankAccount:
    bank_name="SBI"
    ifcs_code="SBINO2346789"
    bank_address="Deoria"
    def __init__(self,an,hn,bal):
        self.account_number=an
        self.holder_name=hn
        self.balance=bal
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print("Insufficient balance")
    def check_balace(self):
        return self.balance
    def display_bank_details(self):
        return f'''
 Bank name={BankAccount.bank_name}
 IFCS Code={BankAccount.ifcs_code}
 Bank Address={BankAccount.bank_address}
 Account number={self.account_number}
 holder number={self.holder_name}
 balance={self.balance}
        '''
obt1=BankAccount(234,"Vishal singh",25000)
obt1.deposit(7000)
print(obt1.check_balace())
print(obt1.withdraw(3000))
print(obt1.check_balace())
print(obt1.display_bank_details())   
student_db={101:{'name':'vishal singh','course':'Data Science','tfees':40000,'pfees':30000,'rfees':10000}}


courses_fees={'Dtat Science':40000,'Web Development':30000,'Testing':20000,'AWS':15000}

while True:
    print('The Kiran Academy'.center(100,'_'))
    print('''
    1.Add Student Record
    2.Display Student Record 
    3.Update Student Record
    4.Delete Student Record 
    5.Filter
    6.LogOut      
          ''')
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        name=input("Name:")
        courses=list(courses_fees.keys())
        sr=1
        for course in courses:
            print(f'{sr}.{course}')
            sr=sr+1
        c_no=int(input("Select Your Course Name:"))
        index=c_no-1
        course=courses[index] 
        fees=courses_fees[course] 
        print(f'course Name:{course}\nCourse Fees:{fees}')  
        dis=eval(input("Enter Discount in Percentage:")) 
        tfees=fees-fees*dis/100
        print(f'Total Fees after {dis} % discount is {tfees}')
        pfees=eval(input('Enter Your Amount:'))
        rfees=tfees-pfees
        reg=len(student_db)+101
        #var[key]=value
        student_db[reg]={'name':name,'course':course,'tfees':tfees,'pfees':pfees,'rfees':rfees}
        print()
        
            
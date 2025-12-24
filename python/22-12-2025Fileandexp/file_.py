# # f=open('file.text','r')
# # for i in f:
# #     print(i)

# #reading=>mode=>'r'
# # f=open('file.text','r')  

# # '''
# # read()
# # '''
# # data=f.read()
# # print(data)


# # '''
# # readline()
# # '''  

# f=open('file.text','r')
# line1=f.readline()
# print(line1)
# line2=f.readline()
# print(line2)

# '''
# readlines()
# '''

# f=open('file.text','r')
# data=f.read(25)
# print(data)
# print(f.tell())
# f.seek(0)
# print(f.tell())
# line1=f.readline()
# print(line1)

# '''
# mode='w'
# '''
# f=open('file.text','w')
# f.write('the kiran academy')
# f.close

# f=open('file.text','w')
# # writelines()
# f.writelines(['java by kiran\n','python by vishal'])
# f.close()

# '''
# append()
# '''
# f=open('file.text','a')
# f.write('welcome')
# f.close

# f=open('file5.text','x')
# f.write('suraj')

#NEW

f=open('file.text','r')


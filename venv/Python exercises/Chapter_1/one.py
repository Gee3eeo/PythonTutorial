rows = eval(input('Enter number of rows: '))
columns = eval(input('Enter number of columns: '))
print('The numbers of objects are', rows*columns)
for i in range(1,columns+1):
    print('*'*i)

for i in range(4):
    print('*'*19)
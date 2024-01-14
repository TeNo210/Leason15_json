with open('models.txt', 'w') as f:
    f.write('****************************************************************************** \n')
    f.write('hello \n')
    f.write('****************************************************************************** \n')
    f.write('hello \n')
    f.write('****************************************************************************** \n')
    f.write('hello \n')
    f.write('****************************************************************************** \n')
    f.write('hello \n')
    f.write('****************************************************************************** \n')
    f.writelines(['1', '2', '3', '4', 'end'])
with open('models.txt','r') as f:
    result = f.read()
    print(result)
with open('models.txt','r') as f:
    result = f.readline()
    print(result)
with open('models.txt','r')as f:
    result = f.readlines()



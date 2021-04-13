file_name = "input.txt"
 
def read():
    fp = open(file_name, "r")
    lst = []
    for line in fp:
        ar = line.split(' ')
        #modify values
        if (ar[0] == 'mayisha'):
            ar[2] = '2.5\n'
            
        lst.append(ar)
    fp.close()
 
    fp = open(file_name, "w")
    for val in lst:
        tmp = str(val[0]) + ' ' + str(val[1]) + ' ' + str(val[2])
        fp.write(tmp)
        
    fp.close()
    print('done')
read()

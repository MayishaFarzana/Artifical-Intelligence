tupleList1= [('parent', 'Habib', 'Rana'),
                   ('parent', 'Habib', 'Panna'),
                   ('parent', 'Habib', 'Shova'),
                   ('parent', 'Habib', 'Ratna'),
                   ('parent', 'Habib', 'Shovon'),
                   ('parent', 'Panna', 'Zahin'),
                   ('parent', 'Panna', 'Labiba'),
                   ('parent', 'Rana', 'Mashrur'),
                   ('parent', 'Rana', 'Mayisha')]

Female=['Shova', 'Ratna', 'Labiba', 'Mayisha']
#find Sister
X=str(input("Name:"))
print('Sister:', end=' ')
flag=0
i=0
while(i<=8):
    if ((tupleList1[i][0] == 'parent')&(tupleList1[i][2] == X)):
        for j in range(9):
            if ((tupleList1[j][0] == 'parent')&(tupleList1[i][1] == tupleList1[j][1]) &( tupleList1[i][2] != tupleList1[j][2])):
    
                for k in Female: 
                    if(tupleList1[j][2] == k):
                        print(tupleList1[j][2], end=' ')
    
    i=i+1

#find Brother
tupleList1= [('parent', 'Habib', 'Rana'),
                   ('parent', 'Habib', 'Panna'),
                   ('parent', 'Habib', 'Shova'),
                   ('parent', 'Habib', 'Ratna'),
                   ('parent', 'Habib', 'Shovon'),
                   ('parent', 'Panna', 'Zahin'),
                   ('parent', 'Panna', 'Labiba'),
                   ('parent', 'Rana', 'Mashrur'),
                   ('parent', 'Rana', 'Mayisha')]

Female=['Shova', 'Ratna', 'Labiba', 'Mayisha']
X=str(input("Name:"))
print('Brother:', end=' ')
i=0
flag = 0
while(i<=8):
    if ((tupleList1[i][0] == 'parent')&(tupleList1[i][2] == X)):
        for j in range(9):
            if ((tupleList1[j][0] == 'parent')&(tupleList1[i][1] == tupleList1[j][1]) &(tupleList1[i][2] != tupleList1[j][2])):
                flag = 0    
                for k in Female: 
                    if(tupleList1[j][2] == k):
                         flag=1   
                if(flag==0):
                    print(tupleList1[j][2], end=' ')
    
    i=i+1


#find Uncle

tupleList1= [('parent', 'Habib', 'Rana'),
                   ('parent', 'Habib', 'Panna'),
                   ('parent', 'Habib', 'Shova'),
                   ('parent', 'Habib', 'Ratna'),
                   ('parent', 'Habib', 'Shovon'),
                   ('parent', 'Panna', 'Zahin'),
                   ('parent', 'Panna', 'Labiba'),
                   ('parent', 'Rana', 'Mashrur'),
                   ('parent', 'Rana', 'Mayisha')]

Female=['Shova', 'Ratna', 'Labiba', 'Mayisha']
X=str(input("Name:"))
print('Uncle:', end=' ')
flag=0
i=0
Z = ""
while(i<=8):
    if ((tupleList1[i][0] == 'parent')&(tupleList1[i][2] == X)):
        Y = tupleList1[i][1]
        for j in range(8):
            if ((tupleList1[j][0] == 'parent')&(tupleList1[i][1] == tupleList1[j][2])):
                Z = tupleList1[j][1]
    i=i+1

m=0
while(m<=8):
    if ((tupleList1[m][0] == 'parent')&(tupleList1[m][1] == Z)):
        if(tupleList1[m][2] != Y):
            flag = 0
            for k in Female:
                if(tupleList1[m][2] == k):
                    flag=1
            if(flag==0):
                print(tupleList1[m][2], end=' ')
                
    m=m+1

#find Aunt
tupleList1= [('parent', 'Habib', 'Rana'),
                   ('parent', 'Habib', 'Panna'),
                   ('parent', 'Habib', 'Shova'),
                   ('parent', 'Habib', 'Ratna'),
                   ('parent', 'Habib', 'Shovon'),
                   ('parent', 'Panna', 'Zahin'),
                   ('parent', 'Panna', 'Labiba'),
                   ('parent', 'Rana', 'Mashrur'),
                   ('parent', 'Rana', 'Mayisha')]

Female=['Shova', 'Ratna', 'Labiba', 'Mayisha']
X=str(input("Name:"))
print('Aunt:', end=' ')
flag=0
i=0
Z = "";
while(i<=8):
    if ((tupleList1[i][0] == 'parent')&(tupleList1[i][2] == X)):
        Y = tupleList1[i][1]
        for j in range(8):
            if ((tupleList1[j][0] == 'parent')&(tupleList1[i][1] == tupleList1[j][2])):
                Z = tupleList1[j][1]   
    i=i+1

m=0
while(m<=8):
    
    if ((tupleList1[m][0] == 'parent')&(tupleList1[m][1] == Z)):
        if(tupleList1[m][2] != Y):
            for k in Female:
                if(tupleList1[m][2] == k):
                    print(tupleList1[m][2], end=' ')


                
    m=m+1



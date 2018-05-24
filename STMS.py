def Fa():
    print('Fa')
ch2='y'
while(ch2=='y' or ch2=='Y'):
    f=open("E:\Study\St.txt","r+")
    l=f.read()
    f.close()
    l=l.split('\n')
    stu={}
    fac={}
    adm={}
    for i in l:    
        i=i.split(':')
        if(i[0]=='S'):
            stu[i[1]] = i[2:]
        elif(i[0]=='F'):
            fac[i[1]] = i[2:]
        elif(i[0]=='A'):
            adm[i[1]] = i[2:]
        elif(i[0]=='D'):
            td=i[1];
        else:
            print('File is Corrupt')
            exit()
    ch=input("Enter The Choice (St/Fa/Ad) : ")
    if(ch=='St'):
        print('Welcome Student')
        ch3='y'
        while(ch3=='y' or ch3=='Y'):
            stn=input('Enter Your Name : ')
            pas=input('Enter The Password : ')
            if((stn in stu)and(pas==stu[stn][4])):
                ch1=input('What Function you want to perform : \n1.Show All Details\n2.Show Fees\n3.Show Rank\n')
                if(ch1=='1'):
                    print("Name : %s"%stn)
                    print("Attendance : %s"%stu[stn][2])
                    print("Marks : %s"%stu[stn][3])
                    print("Rank : %s"%stu[stn][1])
                    print("Fees : %s"%stu[stn][0])
                elif(ch1=='2'):
                    print("Name : %s"%stn)
                    print("Fees : %s"%stu[stn][0])
                elif(ch1=='3'):
                    print("Name : %s"%stn)
                    print("Rank : %s"%stu[stn][1])
                else:
                    print('Choose Correct Option')
            else:
                print("Enter Correct Details")
            ch3=input('Want To Coninue or Not (As Student) :')
    elif(ch=='Fa'):
        print('Welcome Faculty')
        ch3='y'
        while(ch3=='y' or ch3=='Y'):
            fan=input('Enter Your Name : ')
            if((fan in fac)and(fac[fan][0])):
                ch1=input('What do you want to do : \n1.UpdateMarks\n2.UpdateAttend(All)\n3.UpdateAttend(Specififc)\n')
                if(ch1=='1'):
                    stn=input('Enter The Name of Student : ')
                    if(stn in stu):
                        print('Marks of that Student is : %s'%stu[stn][3])
                        stu[stn][3]=input('Enter Updated Marks for that Student : ')
                        temp = []
                        for i in stu:
                            temp.append([i,stu[i][3]])
                        temp=sorted(temp,key=lambda l:l[1],reverse=True)
                        c=1
                        for i in temp:
                            stu[i[0]][1]=str(c)
                            c=c+1
                    else:
                        print('Enter Correct Name')
                elif(ch1=='2'):
                    at=input('Enter Updated Attendance for all')
                    for i in stu:
                            stu[i][2]=at
                elif(ch1=='3'):
                    stn=input('Enter The Name of Student : ')
                    if(stn in stu):
                        print('Attendance of that Student is : %s'%stu[stn][2])
                        stu[stn][2]=input('Enter Updated Attendance for that Student : ')
                    else:
                        print('Enter Correct Name')
                else:
                    print('Choose Correct Option')
            else:
                print("Enter Correct Details")
            ch3=input('Want To Coninue or Not (As Faculty) :')
    elif(ch=='Ad'):
        print('Welcome Admin')
        ch3='y'
        while(ch3=='y' or ch3=='Y'):
            an=input('Enter Your Name : ')
            if((an in adm)and(adm[an][0])):
                ch1=input('What do you want to do : \n1.Total Days\n2.UpdateFees(All)\n3.UpdateFees(Specififc)\n')
                if(ch1=='1'):
                    print('Total Days are : %s'%td)
                    cha=input('Want to Update : ')
                    if(cha=='y' or cha=='Y'):
                        td=input('Enter Updated Value : ')
                elif(ch1=='2'):
                    f=input('Enter Updated Fees for all')
                    for i in stu:
                            stu[i][0]=f
                elif(ch1=='3'):
                    stn=input('Enter The Name of Student : ')
                    if(stn in stu):
                        print('Fees of that Student is : %s'%stu[stn][0])
                        stu[stn][0]=input('Enter Updated Fees for that Student : ')
                    else:
                        print('Enter Correct Name')
                else:
                    print('Choose Correct Option')
            else:
                print("Enter Correct Details")
            ch3=input('Want To Coninue or Not (As Admin) :')
    else:
        print('Enter Correct Details')
    f=open("E:\Study\St.txt","w+")
    f.write('D:%s'%td)
    for i in stu:
        f.write('\nS:%s'%i)
        for j in stu[i]:
            f.write(':%s'%j)
    for i in fac:
        f.write('\nF:%s'%i)
        for j in fac[i]:
            f.write(':%s'%j)
    for i in adm:
        f.write('\nA:%s'%i)
        for j in adm[i]:
            f.write(':%s'%j)
    f.close()
    ch2=input('Want To Coninue or Not :')
#{'Name': ['Fees', 'Rank', 'Attnd','Marks'], 'Bhanu Bisht': ['5000', '1', '87','98']}
#D:1000
#S:Bhanu Bisht:15000:1:80:98
#S:Bqisht:1000:2:80:88
#F:Abc:bb
#F:Na:aa
#A:Xyz:400
#A:Nx:40

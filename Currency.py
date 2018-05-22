ch='y'
f=open("E:\Study\Bhanu.txt","r+")
while(ch=='y'or ch=='Y'):
    c=input("Enter he string in which you want to convert : ")
    d=0
    l = []
    for line in f:
        line=line.split(':')
        line[1]=line[1].split('\n')
        if(c=='INR'):
           if(line[0]=='INR'):
               d=float(line[1][0])
           elif(line[0]=='USD'):
               d=float(line[1][0])/0.015
           elif(line[0]=='Euro'):
               d=float(line[1][0])/0.012
        elif(c=='USD'):
           if(line[0]=='INR'):
               d=float(line[1][0])*0.015
           elif(line[0]=='USD'):
               d=float(line[1][0])
           elif(line[0]=='Euro'):
               d=float(line[1][0])/0.85
        elif(c=='Euro'):
           if(line[0]=='INR'):
               d=float(line[1][0])*0.012
           elif(line[0]=='USD'):
               d=float(line[1][0])*0.85
           elif(line[0]=='Euro'):
               d=float(line[1][0])
        l.append(d)
    for i in l:
        f.write("%s:"%c)
        f.write("%f"%i)
        f.write("\n")
    ch=input("Want to Continue : ")
f.close()

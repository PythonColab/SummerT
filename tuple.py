t1=("Hello",3.5,2)
l1=[]
for i in t1:
    print(i)
for i in t1:
    if(i==3.5):
        i=13.5
    l1.append(i);
del t1
t1=tuple(l1)
for i in t1:
    print(i)

#List & Tuple
"""
li = []
ch ='y'
while(ch=='y'):
    li.append(input("Enter The Input : "))
    ch=input('Want To continue : ')
print(li)
t=tuple(li)
t+=tuple((10,29,30))
print(t)
l2=list(t)
ch ='y'
while(ch=='y'):
    l2.insert(input("Enter The Index : "),input("Enter The Value : "))
    ch=input('Want To continue : ')
t2=tuple(l2)
print(t2)
"""
#Dictionary
"""
dict1 = {}
k=input("Enter The Key : ")
dict1[k] = input("Enter The Value : ")
print(dict1)
print(dict1.keys())
print(dict1.items())
k=input("Enter The Key for search : ")
print(dict1.get(k))
dict1.clear()
print(dict1)
del dict1
"""
#Set
"""
s1=set("Hello This is set test")
s1.add('r')
print(s1)
s1=frozenset("Hello")
print(s1)
"""
#File Handeling
"""
mf=open("E:\Study\St.txt",'a')
print(mf.closed)
if(mf.closed):
    print("Closed")
else:
    print("Open")
mf.close()
mf=open("E:\Study\St1.txt",'a+')
st=input("Hello Every One : ")
mf.write("\n%s"%st)
mf.close()
mf=open("E:\Study\St1.txt",'r+')
for i in mf:
    print(i)
mf.close()
"""
#Functions
"""
def add(a,b):
    return(a+b)
print(add(int(input('Enter A : ')),int(input('Enter B : '))))
"""
#Classes
class c:
    d=30
class ab(c):
    'Class Documentation'
    a=0
    b=0
    def __init__(self,c=10,d=20):
        self.a=int(c)
        self.b=int(d)
    def xyz(self):
        c=self.a+self.b+super().d
        return c
ap = ab(input("Enter A for ap : "))
print(ap.xyz())
app = ab(input("Enter A for app : "),input("Enter B for app : "))
print(app.xyz())


a=int(input("enter the first number"))
b=int(input("enter the second number"))
l=[]
s=[]
def compare(x,y):
    if(x>y):
        l.append(x)
        s.append(y)
    else:
        s.append(y) 
        l.append(x) 
       
compare(a,b)  
print(l)
print(s)     


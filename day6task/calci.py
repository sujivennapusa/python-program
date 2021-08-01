class calci:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
    def fdiv(self,a,b):
        return a//b

n1=int(input("enter the number:"))
n2=int(input("enter the number:"))
myCalci=calci()
print(myCalci.add(n1,n2))
print(myCalci.sub(n1,n2))
print(myCalci.mul(n1,n2))
print(myCalci.div(n1,n2))
print(myCalci.fdiv(n1,n2))




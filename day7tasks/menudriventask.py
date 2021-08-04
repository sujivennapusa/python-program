class AdditionOperation:
    def addTwoNum(self,a,b):
        return a+b
class SubtractionOperation:
    def subTwoNum(self,a,b):
        return a-b
class MultiplicationOperation:
    def mulTwoNum(self,a,b):
        return a*b  
o1=AdditionOperation()
o2=SubtractionOperation()
o3=MultiplicationOperation()        
while(True):        
    print("select an option from menu")
    print("\n")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    choice=int(input("enter the choice :"))
    x=int(input("enter the number :"))
    y=int(input("enter the number :"))
    if choice==1:
        print(o1.addTwoNum(x,y))
    if choice==2:
        print(o2.subTwoNum(x,y))
    if choice==3:
        print(o3.mulTwoNum(x,y))

        


class AdditionOperation:
    def addTwoNum(self,a,b):
        return a+b
class SubtractionOperation:
    def subTwoNum(self,a,b):
        return a-b
class MultiplicationOperation:
    def mulTwoNum(self,a,b):
        return a*b        
class Calculator(AdditionOperation,SubtractionOperation,MultiplicationOperation):
    pass
obj=Calculator()
""" n1=int(input("enter the number:"))
n2=int(input("enter the number:"))
print(obj.addTwoNum(n1,n2))
print(obj.subTwoNum(n1,n2))
print(obj.mulTwoNum(n1,n2)) """
print(issubclass(Calculator,MultiplicationOperation))
print(issubclass(SubtractionOperation,MultiplicationOperation))
print(issubclass(MultiplicationOperation,Calculator))
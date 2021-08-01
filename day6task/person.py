class person:
    def __init__(self,name):
        self.myName=name
    def sayMyName(self):
        print(self.myName)    
n=input("enter name:")
p=person(n)
p.sayMyName()        
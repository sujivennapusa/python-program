class department:
    def __init__(self,dept):
        self.dept=dept
    def addStudent(self):
        self.name=input("enter name:")
        self.rollno=int(input("enter rollno:"))  
        self.admno=int(input("enter admno:"))
        self.addr=input("enter addr:")
        self.clz=input("enter clz:") 
        self.mbno=int(input("enter number:"))  
        print(self.name)
        print(self.rollno)
        print(self.admno)
        print(self.addr)
        print(self.clz)
        print(self.mbno) 
dept1=department("cse")
dept1.addStudent()
dept2=department("ece")
dept2.addStudent()
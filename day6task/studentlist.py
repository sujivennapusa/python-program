#LIST OF OBJECTS
class students:
    def __init__(self,name,rollno,admno):
        self.name=name 
        self.rollno=rollno
        self.admno=admno
obj=[]
obj.append(students("suji",124,1561))        
obj.append(students("sathi",126,1581))    
obj.append(students("nani",129,1761))    
print(obj[0].name)
print(obj[1].name)
print(obj[2].name)
print(obj[0].name)
print(obj[0].rollno)
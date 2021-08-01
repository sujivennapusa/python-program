class employee:
    name="suji"
    def printName(self):
        print(self.name)
employee.printName=classmethod(employee.printName)   
employee.printName()     

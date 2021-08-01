class India:
    def allotNo(self,num):
        self.num=num
        print(num)
class CarManufacturer(India):
    def makeACar(self,brand,color,price):
        print(brand,color,price)
class Seller(CarManufacturer):
    def CustomerOrder(self,name,mobno):
        print(name,mobno)

a=India()
b=CarManufacturer()
c=Seller()          
c.CustomerOrder("navi",9393562869)
c.makeACar("ferari","white","10000000")
c.allotNo("ap022678")

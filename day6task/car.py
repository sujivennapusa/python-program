class cars:
    colour="black"
    brand="bmw"

    def findMileage(self,li,km):
        return km/li


myCar=cars()
a=input("enter the colour")
b=input("enter the brand")

l=int(input("enter the  no.of litres:"))
k=int(input("enter the no.of kilometres"))
mileage=myCar.findMileage(l,k)

myCar.colour=a
myCar.brand=b
print(myCar.colour)
print(myCar.brand) 
#printing default values using objects   
defaultCar=cars()
print(defaultCar.colour)
print(defaultCar.brand)
print(mileage)
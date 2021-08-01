class Cars:
    def mineColor(self,color):
        self.color=color
        print(self.color)

class BMW(Cars):
    def topspeed(self,speed):
        self.speed=speed  
        print(self.speed)       
objcars=Cars() 
objBMW=BMW()
""" objcars.mineColor("red")
objcars.topspeed(100)        """
objBMW.mineColor("red")
objBMW.topspeed(200)

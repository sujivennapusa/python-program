class animal:
    def small(self,name):
        self.name=name
        print(self.name)
class lion(animal):
    def gender(self,color):
        self.color=color
        print(self.color) 

obj1=animal()
obj2=lion()
obj2.gender("female")
obj2.small("lioness")
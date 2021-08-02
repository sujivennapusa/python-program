#Counter()
import collections
l=[]
for people in range(0,10):
    name=input("enter the name:")
    l.append(name)
a=collections.Counter(l)    
print(a)
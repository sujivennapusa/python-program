myfile=open('demo.txt','r+')
""" myfile.write("hello world") """
myfile.write("karnataka is a state in india") 
""" myfile=open('demo.txt','r') """

x=myfile.read()
print(str(x))
myfile.close()
myfile=open('demo.txt','a+')
""" myfile.write("hello world") """
i=input("enter the name:")
myfile.write(i+"\n")
print(myfile.tell())
myfile.seek(0)
""" myfile.write("karnataka is a state in india")  """
""" myfile=open('demo.txt','r') """

x=myfile.read()
print(str(x))
myfile.close()
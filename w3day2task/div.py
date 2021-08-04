import logging
a=int(input("enter number:"))
b=int(input("enter number:"))
x=a/b
logging.basicConfig(filename='division.log',level=logging.DEBUG)
logging.info(x)
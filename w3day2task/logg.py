#logging
import logging
#priority wise 
#logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.DEBUG)

logging.basicConfig(filename="demo.log",level=logging.DEBUG)

""" logging.critical("critical error happened")
logging.error("an unknown error happened")
logging.warning("expected value is integer") """
x=10
y=20
z=x+y
logging.info(z)
#logging.info("normal message")
""" logging.debug("for developers") """
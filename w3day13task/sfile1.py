myfile=('file','w+b')
test=bytearray([12,1,33,12])
myfile.write(test)
myfile.close()
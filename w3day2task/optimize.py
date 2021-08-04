import timeit
print(timeit.timeit(stmt="a=10;b=5;c=a+b"))
print(timeit.timeit(stmt="a=10+65"))

mycode='''85+69'''
print(timeit.timeit(stmt=mycode))

n='''
a=10
if(a<15):
    pass'''
print(timeit.timeit(stmt=n))
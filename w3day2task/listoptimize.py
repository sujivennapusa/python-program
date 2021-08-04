import timeit
li=[123,856,795,459,43,879,765,425,100,365,795,489]
def f1():
    filter (43,li)
def f2():
    for i in li:
        if(i==43):
            pass
print(timeit.timeit(f1,number=100000))                
print(timeit.timeit(f2,number=100000))                
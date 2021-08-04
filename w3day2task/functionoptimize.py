import timeit
def printnumbers():
    for n in range(1000):
        pass
def printwhile():
    n=0
    while(n<=1000):
        n=n+1
        pass
print(timeit.timeit(printnumbers,number=100000))
print(timeit.timeit(printwhile,number=100000))


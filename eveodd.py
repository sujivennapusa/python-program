a=int(input("enter the first number"))
even=[]
odd=[]
def eve(x):
    if(x%2==0):
        even.append(a)
    else:
        odd.append(a)
eve(a)            
print(even)
print(odd)
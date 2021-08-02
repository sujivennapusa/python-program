class RBI:
    def interest(self):
        a=int(input("enter the interest:"))
        print("interest is:",a)
class SBI(RBI):
    def interest(self):
        b=int(input("enter the interest:"))
        print("interest is:",b)

class HDFC(RBI):
    def interest(self):
        c=int(input("enter the interest:"))
        print("interest is:",c)

class ICICI(RBI):
    def interest(self):
        d=int(input("enter the interest:"))
        print("interest is:",d)        
e=RBI()
f=SBI()
g=ICICI()
h=HDFC()
e.interest()
f.interest()
g.interest()
h.interest()


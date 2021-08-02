""" #namedtuple()
import collections
employees=collections.namedtuple('employees',["name","empid","salary"])
e1=employees("raju","10001","25000")
print(e1[0])
 """
""" #OrderedDict()
import collections
d1=collections.OrderedDict()
d1['name']="sony"
d1['rollno']="22"
d1['admno']="1001"

for key,value in d1.items():
    print(key,value) """

""" #Counter()
import collections
x=collections.Counter(["hello","hai","hello"])
print(x) """


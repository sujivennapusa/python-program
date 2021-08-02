#chain map
import collections
dict1={"name":"rahul","age":"22"}
dict2={"name":"suraj","age":"20"}
comb_dict=collections.ChainMap(dict1,dict2)
print(comb_dict.maps)
print(list(comb_dict.keys()))
print(list(comb_dict.values()))
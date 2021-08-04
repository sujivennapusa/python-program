import csv
headercontent=["name","rollno"]
studentdata=[
    {"name":"anu","rollno":"24"},
    {"name":"binny","rollno":"27"},
    {"name":"nani","rollno":"29"},
    {"name":"suji","rollno":"26"},
    {"name":"manu","rollno":"13"},
]

with open('student.csv','w+',encoding='UTF8',newline='') as s:
    writer=csv.DictWriter(s,fieldnames=headercontent)
    writer.writeheader()
    writer.writerows(studentdata)
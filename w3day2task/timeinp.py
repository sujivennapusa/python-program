from datetime import datetime
 
my_string = str(input('Enter date(yyyy-mm-dd): '))
 
 
print(datetime.strptime(my_string, "%Y-%m-%d"))
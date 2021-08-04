import pytz
from datetime import datetime
standard_time=pytz.utc
#time_zone=pytz.timezone("Asia/kolkata")
time_zone=pytz.timezone("Antarctica/McMurdo")
print(datetime.now(standard_time))
print(datetime.now(time_zone).strftime("%Y-%m-%d %H:%M:%S"),time_zone)
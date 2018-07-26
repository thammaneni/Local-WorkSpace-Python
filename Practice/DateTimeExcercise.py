from datetime import date
from datetime import time
from datetime import datetime

today = date.today()
print (today)

print (today.day, today.month, today.year)

today = datetime.now()
print ("Current date is :", today)

time = datetime.time(today)
print ("Current time is : ", time)
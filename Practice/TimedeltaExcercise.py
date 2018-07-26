from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

now = datetime.now()
print ("Today is "+ str(now))

print ("Time after 365 days :"+str(now + timedelta(days=365)))

print ("Date after 6 weeks, 4 days,20hours : ", str(now + timedelta(weeks=6,days=4,hours=20)))
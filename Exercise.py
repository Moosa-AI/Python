import time
    
from datetime import datetime

a=time.strftime('%H:%M:%S')
print(a)
if (a<'12:00:00'):
    print("Good Morning Sir")
elif (a=='12:00:00'):
    print("Good Afternoon Sir")
elif (a>'12:00:00' and a<'19:00:00'):
    print("Good Evening")
else:
    print("Good Night Sir")


now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
print("date and time:",date_time)
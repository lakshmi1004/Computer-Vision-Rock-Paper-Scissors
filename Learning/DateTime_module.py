#%%
#Now working on date module YYY -MM - DD
import datetime
from datetime import date
from time import strftime
from xmlrpc.client import _iso8601_format
#Getting dates 
d = datetime.date(2020,1,2) #if use month or dates '0' on statrts throws invalid token syntax eror.
print(d)
# %%
#todays date
today = datetime.date.today()
print(today)
# %%
print(today.day)
print(today.year)
print(today.month)
# %%
print(today.weekday())
#For weekday() - Monday 0, Tuesday 1 - Sunday 6

# %%
#isoweekday
print(today.isoweekday())
#For isoweekday() - Monday 1, Tuesday 2 - Sunday 7

# %%
#time_delta
bday = datetime.date(1985,4,10)
tdelta = datetime.timedelta(days =4)
print(today + tdelta)

# %%
#date difference
till_bday = today - bday
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())
# %%
#Now working on time module HH MM SS
import datetime
t = datetime.time(16,4,15,200000)
print(t)
print(t.hour)
print(t.second)

# %%
#Now working on date & time module
dt = datetime.datetime(2020,5,14,16,4,15,200000)
print(dt)
print(dt.hour)
print(dt.date())
print(dt.time())

# %%
#today/Now/utc
dt_today = datetime .datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()
print(dt_today)
print(dt_now)# today & now are looks same but in tme zone it is different
print(dt_utcnow)




# %%
import pytz
dt_today = datetime.datetime(2022,4,8,5,12,15,tzinfo=pytz.UTC)
dt_now = datetime.datetime.now(tz = pytz.UTC)
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo = pytz.UTC)
print(dt_today)
print(dt_now)
print(dt_utcnow)

# %%
#To get all time zones
for tz in pytz.all_timezones:
    print(tz)
# %%
dt_utcnow = datetime.datetime.now()
dt_gmt = dt_utcnow.astimezone(pytz.timezone('GB'))
print(dt_gmt)


# %%
#iso8601_format - see python datetime documentto display the date as u wish
dt_gmt = dt_utcnow.astimezone(pytz.timezone('GB'))
print(dt_gmt.strftime('%B %d,%Y'))
#strftime - converts Datetime to String
#strptime - converts String to Datetime

# %%

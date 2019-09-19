from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

dt_now = datetime.now()
day_delta = timedelta(days=1)
month_delta = dt_now + relativedelta(months=-1)

yersterday = dt_now - day_delta
print(yersterday.strftime('%Y-%m-%d'))
print(dt_now.strftime('%Y-%m-%d'))
print(month_delta.strftime('%Y-%m-%d'))

date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)
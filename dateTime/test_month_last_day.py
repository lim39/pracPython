#import calendar
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + timedelta(days=4)  # this will never fail
    # print(any_day)
    # print(any_day.replace(day=28))
    # print(next_month)
    # print(timedelta(days=next_month.day))
    return next_month - timedelta(days=next_month.day)

# today = datetime.today()
# last_day = last_day_of_month(today)
# print(last_day.strftime("%Y-%m-%d"))
print(datetime.today())
lastmonthday= datetime.today() - relativedelta(months=1)
print(lastmonthday)
lastmonth_lastday = last_day_of_month(lastmonthday)
print(lastmonth_lastday.strftime("%Y-%m-%d"))
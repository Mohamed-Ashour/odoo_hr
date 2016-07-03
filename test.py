from datetime import datetime
from datetime import date
import calendar
from datetime import timedelta
from dateutil.relativedelta import relativedelta
my_date = datetime.today()
calendar.day_name[my_date.weekday()]

print datetime.today().weekday()
print calendar.day_name[my_date.weekday()]




print 'Today: ',datetime.now().strftime('%d/%m/%Y %H:%M:%S')
date_after_month = datetime.now()+ relativedelta(days=1)
print 'After 5 Days:', date_after_month.strftime('%d/%m/%Y')
d = date.today()

print datetime.combine(d, datetime.min.time())
import datetime
testeddate = '4/25/2015'
dt_obj = datetime.strptime(testeddate,'%m/%d/%Y')
#print 'Today: ',datetime.now().strftime('%d/%m/%Y')
#date_after_month = datetime.now()+ relativedelta(day=1)
#print 'After a Days:', date_after_month.strftime('%d/%m/%Y')
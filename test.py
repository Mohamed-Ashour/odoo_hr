from datetime import datetime
import calendar
from datetime import timedelta
from dateutil.relativedelta import relativedelta
my_date = datetime.today()
calendar.day_name[my_date.weekday()]

print datetime.today().weekday()
print calendar.day_name[my_date.weekday()]




print 'Today: ',datetime.now().strftime('%d/%m/%Y')
date_after_month = datetime.now()+ relativedelta(days=1)
print 'After 5 Days:', date_after_month.strftime('%d/%m/%Y')

#print 'Today: ',datetime.now().strftime('%d/%m/%Y')
#date_after_month = datetime.now()+ relativedelta(day=1)
#print 'After a Days:', date_after_month.strftime('%d/%m/%Y')
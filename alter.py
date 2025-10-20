from datetime import datetime
from dateutil import relativedelta
import sys

print(sys.argv[1])
format_code = "%d.%m.%Y"
parsed_date = datetime.strptime(sys.argv[1], format_code)
now = datetime.now()

delta = relativedelta.relativedelta(now, parsed_date)
diff = (now - parsed_date).days
print(delta.years, 'Years,', delta.months, 'months,', delta.days, 'days')
print('overall', diff, 'days.')

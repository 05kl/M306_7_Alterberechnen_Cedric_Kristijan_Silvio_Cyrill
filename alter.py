from datetime import datetime
from dateutil import relativedelta
import sys

format_code = "%d.%m.%Y"
parsed_date = datetime.strptime(sys.argv[1], format_code)
now = datetime.now()

delta = relativedelta.relativedelta(now, parsed_date)
diff = (now - parsed_date).days
print('Das Alter ist', delta.years, 'Jahre', delta.months, 'Monate und', 
      delta.days, 'Tage, das sind', diff, 'Tage')

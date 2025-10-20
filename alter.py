from datetime import datetime
import sys

print(sys.argv[1])
format_code = "%d.%m.%Y"
parsed_date = datetime.strptime(sys.argv[1], format_code)
now = datetime.now()
diff = now - parsed_date
print(diff.years)


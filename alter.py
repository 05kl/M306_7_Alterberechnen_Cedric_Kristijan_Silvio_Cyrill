from datetime import datetime
from dateutil import relativedelta
import sys

# Prüfen, ob ein Input Parameter vorhanden ist
if len(sys.argv) < 2:
    print('Error: Kein Input Parameter vorhanden.')
    exit(1)

# Prüfen, ob Datenformat richtig ist
try:
    format_code = "%d.%m.%Y"
    # Nimmt den ersten Parameter im Argument und verarbeitet ihn
    parsed_date = datetime.strptime(sys.argv[1], format_code)
except Exception as e:
    print('Error: Kein richtiges Datenformat.')
    exit(1)

# Nimmt das heutige Datum
now = datetime.now()

# Unterschied nur in Tagen
diff = (now - parsed_date).days

# Prüfen, ob das Datum in der Zukunft liegt
if diff < 0:
    print('Error: Datum in der Zukunft.')
    exit(1)

# Relatives Datum mit dateutil
delta = relativedelta.relativedelta(now, parsed_date)

print('Das Alter ist', delta.years, 'Jahre', delta.months, 'Monate und', 
      delta.days, 'Tage, das sind', diff, 'Tage')

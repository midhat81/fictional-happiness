from datetime import datetime
import pytz

# current Datetime
unaware = datetime.now()
print('Timezone naive:', unaware)

# Standard UTC timezone aware Datetime
aware = datetime.now(pytz.utc)
print('Timezone Aware:', aware)

# UK/Central timezone datetime
aware_uk_central = datetime.now(pytz.timezone('UK/Central'))
print('UK Central DateTime', aware_uk_central)
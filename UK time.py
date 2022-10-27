import pytz
from datetime import datetime
tz = pytz.timezone('UTC')
naive_time = datetime.strptime('2016-04-05 15:00', '%Y-%m-%d %H:%M')
tz_time = tz.localize(naive_time)
london_tz = pytz.timezone('Europe/London')
london_time = tz_time.astimezone(london_tz)
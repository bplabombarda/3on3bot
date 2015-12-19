from datetime import datetime
import json
import os

# =====================================================================
# Load schedule
# =====================================================================
with open('20152016schedule.json', 'r') as schedule_file:
    data = schedule_file.read()
    schedule = json.loads(data)

for game in schedule:
    date = game['est'].split(" ")[0]
    time = game['est'].split(" ")[1]
    hour = time.split(":")[0]
    today = datetime.strftime(datetime.now(), '%Y%m%d')
    currtime = datetime.strftime(datetime.now(), '%H')

    if date == today and (currtime >= str(int(hour) - 3)):
        os.system("python tweeter_v2.py")

    elif:


# print(today, currtime, hour)

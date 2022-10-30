import requests
import dateutil.parser
import pytz
import os
from datetime import datetime, timedelta
import helper

config = helper.read_config()
cat = pytz.timezone("Africa/Johannesburg")
cmd = config['ESPSettings']['Command']

url = config['ESPSettings']['Url']
querystring = {"id":config['ESPSettings']['Area'],"test":"current"}
headers = {"Token": config['ESPSettings']['ApiToken']}

def get_next_blackout(data):
    events = data["events"][0]
    print(events)
    start_date = dateutil.parser.parse(events["start"])
    return cat.normalize(start_date.astimezone((cat)))

response = requests.request("GET", url, data="", headers=headers, params=querystring)

if response:
    print(response.json())
    data = response.json()
    next_blackout = get_next_blackout(data)
    now = datetime.now()
    shutdown_time = next_blackout - timedelta(minutes=1)
    if next_blackout <= now.astimezone(cat) + timedelta(hours=1):
        print("Next blackout is at " + str(next_blackout))
        print(cmd + shutdown_time.strftime("%H:%M"))
        os.system(cmd + str(now.hour) + ':59')
    else:
        print("No need to panic. Next blackout is at " + str(next_blackout))
else:
    print('Unsuccessful request')


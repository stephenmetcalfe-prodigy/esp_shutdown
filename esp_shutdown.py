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
querystring = {"id":config['ESPSettings']['Area']} # Use for production. Uses quota
# querystring = {"id":config['ESPSettings']['Area'],"test":"future"} # Use this for development
headers = {"Token": config['ESPSettings']['ApiToken']}

def get_next_blackout(data):
    events = data["events"][0]
    start_date = dateutil.parser.parse(events["start"])
    return cat.normalize(start_date.astimezone((cat)))

response = requests.request("GET", url, data="", headers=headers, params=querystring)

if response:
    data = response.json()
    next_blackout = get_next_blackout(data)
    now = datetime.now()
    shutdown_time = next_blackout - timedelta(minutes=1)
    if next_blackout <= now.astimezone(cat) + timedelta(hours=1):
        print("Next blackout is at " + str(next_blackout))
        os.system(cmd + str(now.hour) + ':59')
    else:
        print("No need to panic. Next blackout is at " + str(next_blackout))
else:
    print('Unsuccessful request')


import requests
import dateutil.parser
import logging
import pytz
import os
from datetime import datetime, timedelta
import helper

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)
config = helper.read_config()
cat = pytz.timezone("Africa/Johannesburg")
cmd = config['ESPSettings']['Command']
shutdown_message = config['ESPSettings']['ShutdownMessage']

url = config['ESPSettings']['Url']
querystring = {"id":config['ESPSettings']['Area']} # Use for production. Counts towards quota
if config['ESPSetting']['Test'] == True:
    querystring = {"id":config['ESPSettings']['Area'],"test":"future"} # Use this for development
headers = {"Token": config['ESPSettings']['ApiToken']}

def get_next_blackout(data):
    events = data["events"][0]
    start_date = dateutil.parser.parse(events["start"])
    return cat.normalize(start_date.astimezone((cat)))

logging.debug("Getting updates from api")
response = requests.request("GET", url, data="", headers=headers, params=querystring)

if response:
    data = response.json()
    next_blackout = get_next_blackout(data)
    now = datetime.now()
    shutdown_time = next_blackout - timedelta(minutes=1)
    shutdown_time = shutdown_time.strftime("%H:%M")
    if next_blackout <= now.astimezone(cat) + timedelta(hours=1):
        logging.info("Next blackout is at " + str(next_blackout))
        cmd += ' ' + shutdown_time + ' ' + shutdown_message
        os.system(cmd)
    else:
        logging.debug("No need to panic. Next blackout is at " + str(next_blackout))
else:
    logging.error('Unsuccessful request')


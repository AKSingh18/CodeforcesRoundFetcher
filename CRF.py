from plyer import notification
from plyer.utils import platform
from datetime import datetime
from dateutil import tz
import requests
import json
import socket
import os

REMOTE_SERVER = "one.one.one.one"

# source = https://stackoverflow.com/a/918178/13618871
def get_path_to_icon():
  dirname = os.path.dirname(__file__)
  path = os.path.join(dirname, 'files/code-forces') +  (".ico" if platform == "win" else ".png")
  return path

# source = https://stackoverflow.com/a/20913928/13618871
def is_connected(hostname=REMOTE_SERVER):
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(hostname)
    # connect to the host -- tells us if the host is actually reachable
    s = socket.create_connection((host, 80), 2)
    s.close()
    return True
  except Exception:
     pass # we ignore any errors, returning False
  return False

# source = https://www.geeksforgeeks.org/python-desktop-notifier-using-plyer-module/
def notify(title, message):
    
    notification.notify(
        title = title,
        message = message,
        app_icon = get_path_to_icon(),
        timeout = 3)
    
    return

# source = https://stackoverflow.com/a/4771733/13618871
# minor modifications done
def get_date(unix_time_stamp):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()

    utc = datetime.utcfromtimestamp(next_contest['startTimeSeconds'])
    utc = utc.replace(tzinfo=from_zone)
    local = utc.astimezone(to_zone)
                                                          
    return local.strftime('%d-%m-%Y %H:%M')

# Check if the internet connection is available or not
if not is_connected():
   notify("CRF Error", "No internet connection available.")
   exit

response_API = requests.get("https://codeforces.com/api/contest.list")

if (response_API.status_code == 200):  
    
    try:
      contest_list = json.loads(response_API.text)["result"]
      upcoming_contest = list(filter(lambda contest: contest['phase'] == 'BEFORE', contest_list))    
      next_contest = min(upcoming_contest, key=lambda contest: contest['startTimeSeconds'])
      notify(next_contest['name'], get_date(next_contest['startTimeSeconds']))

    except json.decoder.JSONDecodeError:
       notify("CRF Error", "Codeforces is temporarily unavailable.")
       
# Unable to fetch contest list
else:
   notify("CRF Error", "Could not fetch contest list.")
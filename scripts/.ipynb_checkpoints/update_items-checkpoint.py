import pandas as pd
import numpy as np
import requests
import json
from osrs_fcns import unix_conv
from datetime import datetime

headers = {'User-Agent':'GEoutlier-detection_item_update'}
api_endpt = "https://prices.runescape.wiki/api/v1/osrs"
items_endpt = "/mapping"

#get updated items list
items_response = requests.get((api_endpt+items_endpt), headers=headers)
all_items = pd.DataFrame.from_dict(json.loads(items_response.text))

#get current time
current_time = datetime.now()
timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

#save to csv
all_items.to_csv(f'osrs_items-{timestamp}.csv',index=False)

all_items.to_csv('latest_osrs_items.csv',index=False)
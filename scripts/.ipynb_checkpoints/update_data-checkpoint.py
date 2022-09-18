import pandas as pd
import numpy as np
import requests
import json
from osrs_fcns import unix_conv

headers = {'User-Agent':'GEoutlier-detection_5m_update'}
api_endpt = "https://prices.runescape.wiki/api/v1/osrs"
five_min_endpt = "/5m"

#get updated transactions
five_min_response = requests.get((api_endpt+five_min_endpt), headers=headers)
five_min_data = pd.DataFrame.from_dict(json.loads(latest_response.text[8:-1]),orient='columns').T
five_min_data['id'] = five_min_data.index

#changing datetimes
five_min_data.highTime = unix_conv(five_min_data,'highTime')
five_min_data.lowTime = unix_conv(five_min_data,'lowTime')

#the id columns for the latest data and five_min data needs to be changed to an int64 type
five_min_data.id = five_min_data.id.astype('int64')

latest_items = pd.read_csv('latest_osrs_items.csv')

all_w_latest = latest_items.merge(five_min_data,on='id')

#get current time
current_time = datetime.now()
timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")


all_w_latest.to_csv(f'item_prices_{all_w_latest['lowTime'][0]}')
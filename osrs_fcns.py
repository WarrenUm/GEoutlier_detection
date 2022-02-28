import pandas as pd
import numpy as np
import requests
import json
from datetime import datetime

def unix_conv(df,col):
    converted_col = pd.to_datetime(df[col], unit='s')
    
    return pd.DataFrame(converted_col, columns=[col])

def update_data():
    '''Gets the latest 5 minute transaction data. Reads in the latest item_lists and merges the 5 minute data into the latest items dataframe. Saves the 5 minute prices with all the item data with a timestamp and also returns the dataframe.'''
    
    headers = {'User-Agent':'GEoutlier-detection_5m_update'}
    api_endpt = "https://prices.runescape.wiki/api/v1/osrs"
    five_min_endpt = "/5m"

    #get updated transactions
    five_min_response = requests.get((api_endpt+five_min_endpt), headers=headers)
    five_min_data = pd.DataFrame.from_dict(json.loads(five_min_response.text[8:-1]),orient='columns').T
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
    timestamp = current_time.strftime("%Y-%m-%d %H-%M-%S")
    
    latest_time = str(all_w_latest['lowTime'][0].strftime("%Y-%m-%d %H-%M-%S"))
    
    all_w_latest.to_csv(f'item_prices_{latest_time}')
    
    return all_w_latest

def update_items():
    '''Gets an updated list of all items. Saves dataframe with a timestamp and one just called latest_osrs_items. Returns the updated dataframe as well.'''
    
    
    headers = {'User-Agent':'GEoutlier-detection_item_update'}
    api_endpt = "https://prices.runescape.wiki/api/v1/osrs"
    items_endpt = "/mapping"

    #get updated items list
    items_response = requests.get((api_endpt+items_endpt), headers=headers)
    all_items = pd.DataFrame.from_dict(json.loads(items_response.text))

    #get current time
    current_time = datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d %H-%M-%S")

    #save to csv
    all_items.to_csv(f'osrs_items-{timestamp}.csv',index=False)

    all_items.to_csv('latest_osrs_items.csv',index=False)
    
    return all_items
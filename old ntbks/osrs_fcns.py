import pandas as pd
import numpy as np
import requests
import json
from datetime import datetime
import sqlite3
from sqlite3 import Error

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
    five_min_data = pd.DataFrame.from_dict(json.loads(five_min_response.text))
    five_min_timestamp = pd.DataFrame.from_dict(json.loads(five_min_response.text))['timestamp']
    five_min_data_data = pd.json_normalize(five_min_data['data'])
    five_min_data_data.index = five_min_data.index
    five_min_data_data['timestamp'] = five_min_timestamp
    five_min_data = five_min_data_data
    five_min_data['id'] = five_min_data.index

    #changing datetimes
    #five_min_data.highTime = unix_conv(five_min_data,'timestamp')
    #five_min_data.lowTime = unix_conv(five_min_data,'timestamp')

    #the id columns for the latest data and five_min data needs to be changed to an int64 type
    five_min_data.id = five_min_data.id.astype('int64')

    latest_items = pd.read_csv('latest_osrs_items.csv')

    all_w_latest = latest_items.merge(five_min_data,on='id')

    #get current time
    current_time = datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d %H-%M-%S")
    
    #latest_time = str(all_w_latest['timestamp'][0].strftime("%Y-%m-%d %H-%M-%S"))
    
#     five_min_data.to_csv(f'prices/item_prices_{timestamp}.csv',index=False)
    
    return five_min_data

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
    all_items.to_csv(f'items/osrs_items-{timestamp}.csv',index=False)

    all_items.to_csv('latest_osrs_items.csv',index=False)
    
    return all_items


def add_prices(conn, item):
    """
    Create a new project into the items table
    :param conn:
    :param item:
    :return: item id
    """
    sql = ''' INSERT INTO prices(item_id,timestamp,avgHighPrice,highPriceVolume,avgLowPrice,lowPriceVolume)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, item)
    conn.commit()
    return cur.lastrowid

#connection

def create_connection(db_file):
    """Create conn to sqlite db"""
    
    conn = None
    
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def update_local_price_db():
    
    '''Get updated prices from ge api. Add them to the prices table in geitems.db'''
    
    conn = sqlite3.connect('geitems.db')
    cur = conn.cursor()
    
    price_df = update_data()
    
    for row in range(0,len(price_df)):
        item_id = int(price_df.iloc[row]['id'])
        timestamp = int(price_df.iloc[row]['timestamp'])
        avghigh = float(price_df.iloc[row]['avgHighPrice'])
        highvol = int(price_df.iloc[row]['highPriceVolume'])
        avglow = float(price_df.iloc[row]['avgLowPrice'])
        lowvol = int(price_df.iloc[row]['lowPriceVolume'])

    
        price = (item_id,timestamp,avghigh,highvol,avglow,lowvol);
        price_id = add_prices(conn, price)
    
    conn.close()
import pandas as pd
import numpy as np
import requests
import json
from datetime import datetime
import sqlite3
from sqlite3 import Error
import csv
import os
from tqdm.notebook import tqdm_notebook
from tqdm import tqdm
import time
import shutil
<<<<<<< HEAD
=======
from time import perf_counter_ns
>>>>>>> 6c41324c24f06dc2820fb9c503f00a74ebe0678a

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


def add_prices(contents,conn):
    """
    Create a new project into the items table
    :param conn:
    :param item:
    :return: item id
    """
    sql = ''' INSERT INTO prices(item_id,timestamp,avgHighPrice,highPriceVolume,avgLowPrice,lowPriceVolume)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.executemany(sql, contents)
    conn.commit()
    return cur.lastrowid

#connection

def create_connection(db_file):
    """Create conn to sqlite db"""
    
    conn = None
    
    try:
        conn = sqlite3.connect(db_file)
#         print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def update_local_price_db():
    
    '''Get updated prices from ge api. Add them to the prices table in geitems.db'''
    
    conn = sqlite3.connect('../geitems.db')
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
    
def get5mItemData(timestamp):
    headers = {'User-Agent':'GEoutlier-detection'}
    api_endpt = "https://prices.runescape.wiki/api/v1/osrs"
    five_min_timestamp = "/5m?timestamp="
    items_response = requests.get((api_endpt+five_min_timestamp+str(timestamp)), headers=headers)
    five_min_timestamp = pd.DataFrame.from_dict(json.loads(items_response.text))['timestamp']
    five_min_data = pd.DataFrame.from_dict(json.loads(items_response.text)['data']).T
    if(len(five_min_data)>0):
        five_min_data['timestamp'] = five_min_timestamp
        five_min_data['item_id'] = five_min_data.index
        five_min_data.reset_index(drop=True,inplace=True)
        five_data = pd.DataFrame(columns=['item_id','timestamp','avgHighPrice','highPriceVolume','avgLowPrice','lowPriceVolume'])
        five_data.item_id = five_min_data.item_id
        five_data.timestamp = five_min_data.timestamp
        five_data.avgHighPrice = five_min_data.avgHighPrice
        five_data.highPriceVolume = five_min_data.highPriceVolume
        five_data.avgLowPrice = five_min_data.avgLowPrice
        five_data.lowPriceVolume = five_min_data.lowPriceVolume
        return five_data
    else:
        return five_min_data
    

#write current timestamp to file and pass as a param. look for last timestamp and continue from there iterating
def getLatestTimestamp(file):
    #open file
    file = open(file,'r')
    #read line
#     print("Reading New time")
    timeLine = file.readline()
    #close file
    file.close()
    
    return int(timeLine)

def updateTimeFile(newTime,file):
    #open file
    file = open(file,'w')
    #overwrite first line with used timestamp
#     print(f'Updating Time File With: {newTime}')
    file.writelines(newTime)
    #close file
    file.close()
    return newTime

def incrementTime(oldTime):
#     print('Incrementing Time')
    return oldTime + 300

def addLatestData(itemdf):
#     print('Connecting to Database')
    conn = create_connection('../geitems.db')
    for row in range(0,len(itemdf)):
        item_id = int(itemdf.iloc[row]['item_id'])
        timestamp = int(itemdf.iloc[row]['timestamp'])
        avghigh = float(itemdf.iloc[row]['avgHighPrice'])
        highvol = int(itemdf.iloc[row]['highPriceVolume'])
        avglow = float(itemdf.iloc[row]['avgLowPrice'])
        lowvol = int(itemdf.iloc[row]['lowPriceVolume'])

    
    price = (item_id,timestamp,avghigh,highvol,avglow,lowvol);
#     print('Adding Data To Table')
    price_id = add_prices(conn, price)
#     print('Disconnecting from Database')
    conn.close()
    
def write_to_csv(reorg_df):
    tempName = 'tempcsv.csv'
    reorg_df.to_csv(tempName,header=False,index=False)
    return tempName

def readContents(fileName):
    contents = csv.reader(open(fileName))
    return contents

def reorg_df(price_df):
#     print(price_df.columns)
    reorg_df = pd.DataFrame(columns=['item_id','timestamp','avgHighPrice','highPriceVolume','avgLowPrice','lowPriceVolume'])
    
    try:
        reorg_df['item_id'] = price_df['item_id'].astype(int)
    except:
        reorg_df['item_id'] = price_df['id'].astype(int)
        
    reorg_df['timestamp'] = price_df['timestamp'].astype(int)
    reorg_df['avgHighPrice'] = price_df['avgHighPrice'].astype(float)
    reorg_df['highPriceVolume'] = price_df['highPriceVolume'].astype(int)
    reorg_df['avgLowPrice'] = price_df['avgLowPrice'].astype(float)
    reorg_df['lowPriceVolume'] = price_df['lowPriceVolume'].astype(int)
    return reorg_df

def addCSV_ToDB(next_df,conn):
    
    newdf = reorg_df(next_df)
    temp_name = write_to_csv(newdf)
    contents = readContents(temp_name)
    add_prices(contents,conn)
    
    
def getCSVList():
    # folder path
    dir_path = 'Data_CSVs'
    # list to store files
    res = []
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
    return res

def Get_LatestPriceCSVs():
    
    now = round(datetime.timestamp(datetime.now()))
    newTime = getLatestTimestamp('latestTime.txt')
    timeRange = range(newTime,now,300)
    for i in tqdm(timeRange):
#         print('Getting TimeStamp Data')
        newData = get5mItemData(newTime)
        
        newData.to_csv(f'Data_CSVs/price_data_{newTime}.csv')
        
        newTime = incrementTime(newTime)
        
        updateTimeFile(str(newTime),'latestTime.txt')
        time.sleep(np.random.randint(0,3))
    return

def runTableAdder():
    csvList = getCSVList()
    conn = create_connection('../geitems.db')
#     print(csvList)
    for i in tqdm(csvList):
        dfName = 'Data_CSVs\\'+i
        
        price_df = pd.read_csv(dfName)
        price_df.drop('Unnamed: 0',axis=1,inplace=True)
        shutil.move(dfName,'Imported\\'+i)
        if(len(price_df) == 0):
#             print('No Columns!')
            continue
        #move dfName to folder called Imported
        
        addCSV_ToDB(price_df,conn)
    
    conn.close()

def queryDB(query):
    conn = sqlite3.connect('../geitems.db')
    response = conn.cursor().execute(query).fetchall()
    conn.close()
    return response

def getLatestItemMap(idFirst=True):
    headers = {'User-Agent':'GEoutlier-detection'}
    api_endpt = "https://prices.runescape.wiki/api/v1/osrs"
    items_endpt = "/mapping"
    try:
        items_response = requests.get((api_endpt+items_endpt), headers=headers)
        all_items = pd.DataFrame.from_dict(json.loads(items_response.text))
        all_items.to_csv('latestItemsList.csv')
    
    except:    
        #default to saved most recent if can't get
        all_items = pd.read_csv('latestItemsList.csv',index_col=0)
        
    itemDict = {}
    idSeries = pd.Series(all_items['id'])
    nameSeries = pd.Series(all_items['name'])
    if(idFirst):
        for i,val in enumerate(idSeries):
            itemDict[val] = nameSeries[i]
    else:
        for i,val in enumerate(nameSeries):
            itemDict[val] = idSeries[i]
    return itemDict
    
def cleanItemDF(df):
    df.members = df.members.astype(bool)
    df.drop('id',inplace=True,axis=1)
    return df

def cleanPriceDF(df):
    #format timestamp and replace empty str with np.nan
    df.timestamp = pd.to_datetime(df.timestamp,unit='s')
    df.avgHighPrice.replace('',np.nan,inplace=True)
    df.avgLowPrice.replace('',np.nan,inplace=True)
    df.set_index('timestamp',inplace=True)
    df.drop('id',inplace=True,axis=1)
    return df

def formatPriceDF(response):
    df = pd.DataFrame(response,columns=['id','item_id','timestamp','avgHighPrice','highPriceVolume','avgLowPrice','lowPriceVolume'])
    return df

def formatItemDF(response):
    df = pd.DataFrame(response,columns=['id','item_id','members','lowalch','buyLimit','value','highalch','icon','name','examine'])
    return df

def getItemInfo(item):
    if(type(item) == str):
        mapping = getLatestItemMap(idFirst=False)
        itemID = mapping[item]
        itemInfo = cleanItemDF(formatItemDF(queryDB(f"""SELECT * from items WHERE item_id = {itemID} LIMIT 1""")))
    else:
        itemID = item
        itemInfo = cleanItemDF(formatItemDF(queryDB(f"""SELECT * from items WHERE item_id = {itemID} LIMIT 1""")))
        
    return itemInfo

def getItemPrices(items,dateBegin,dateEnd):
    t1_start = perf_counter_ns()    
    #convert dateStr to dtObj and then to seconds
    dateStart = convertDateToTimestamp(dateBegin)
    dateEnd = convertDateToTimestamp(dateEnd)
    t_dtconvert = perf_counter_ns()
    print('Time to convert dates:',(t_dtconvert-t1_start)/1000000000)
    
    #convert each itemName to item_id
    print('Mapping Names To IDs')
    mapping = getLatestItemMap(idFirst=False)
    item_ids = []
    for i in items:
        item_ids.append(mapping[i])
    t_mapping = perf_counter_ns()
    print('Time to map item names:',(t_mapping-t_dtconvert)/1000000000)
    
    print('Querying DB')
    fullDF = cleanPriceDF(formatPriceDF(queryDB(f"""SELECT * from prices WHERE timestamp > {dateStart} AND timestamp < {dateEnd}""")))
    t_query = perf_counter_ns()
    print('Time to query DB:',(t_query-t_mapping)/1000000000)

    print('Filtering DB')
    filteredDF = fullDF.loc[fullDF['item_id'].isin(item_ids)]
    t_filter = perf_counter_ns()
    print('Time to filter DF:',(t_filter-t_query)/1000000000)
    return filteredDF

def convertDateToTimestamp(dateStr):
    dtObj = datetime.strptime(dateStr, '%d/%m/%y %H:%M:%S').timestamp()
    return dtObj

def resampleDF(df,resampleStr):
    return df.resample(resampleStr).mean()

        
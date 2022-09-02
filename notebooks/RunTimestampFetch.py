import pandas as pd
import numpy as np
import requests
import json
from datetime import datetime
from osrs_fcns import *
import datetime
import time


def main():
    
    
    newTime = getLatestTimestamp('latestTime.txt')
    while(newTime <= round(datetime.datetime.timestamp(datetime.datetime.now()))):
        print('Getting TimeStamp Data')
        newData = get5mItemData(newTime)
        if(len(newData)>0):
            addLatestData(newData)
        
        newTime = incrementTime(newTime)
        
        updateTimeFile(str(newTime),'latestTime.txt')
        time.sleep(np.random.randint(0,3))
    return

main()
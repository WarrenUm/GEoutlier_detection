import pandas as pd
import numpy as np
import requests
import json
from osrs_fcns import *
import schedule
import time

print('Starting Script')

schedule.every(5).minutes.do(update_local_price_db)

while True:
    schedule.run_pending()
    time.sleep(1)
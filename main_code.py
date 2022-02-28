import pandas as pd
import numpy as np
import requests
import json
from datetime import datetime
from osrs_fcns import *
import time


starttime = time.time()

if (30.0 - ((time.time() - starttime) % 30.0)):
    print('Updating_latest')
    update_data()
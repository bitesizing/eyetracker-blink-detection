# %%
""" File to record from the eyetracker for a given period of time, and save the data. """

# 'Import' code (pull in code that tobii etc. have written so we can use it)
import time
from helpers import EyetrackerHandler

# Fill out manually - all subscriptions listed in subscriptions_list.txt
subscriptions_list = ['eyetracker_gaze_data']

# Setup eyetracker, record for 2s, then sleep
eyetracker = EyetrackerHandler(subscriptions_list)
eyetracker.subscribe()
time.sleep(10)
eyetracker.unsubscribe()

""" Save eye images and gaze data to json files. """
eyetracker.write_files()

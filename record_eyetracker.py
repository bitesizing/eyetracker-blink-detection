# %%
""" File to record from the eyetracker for a given period of time, and save the data. """
import time
from helpers import EyetrackerHandler

# Manually list all the data sources to record - options are listed in `helper-files/subscriptions_list.txt`
subscriptions_list = [
    'eyetracker_gaze_data',
    ]
recording_time = 10  # time to record in seconds

# Toy code to set up the eyetracker, record for desired number of seconds, then sleep
eyetracker = EyetrackerHandler(subscriptions_list)  # set up the eytracker as an 'object' with the given subscriptions
eyetracker.subscribe()  # start recording
time.sleep(recording_time)  # wait 10s
eyetracker.unsubscribe()  # stop recording

""" Save eye images and gaze data to json files. """
eyetracker.write_files()

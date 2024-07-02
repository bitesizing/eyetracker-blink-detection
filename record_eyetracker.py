""" File to record from the eyetracker for a given period of time, and save the data. """

# %%
# 'Import' code (pull in code that tobii etc. have written so we can use it)
import json
import time
import numpy as np
import tobii_research as tr
from tobiiresearch.implementation.EyeTracker import EyeTracker, find_all_eyetrackers
from helpers import save_eye_images_as_png, write_file, EyetrackerHandler

# Fill out manually - all subscriptions listed in subscriptions_list.txt
subscriptions_list = ['eyetracker_gaze_data', 'eyetracker_eye_images']

# Setup eyetracker, record for 2s, then sleep
eyetracker = EyetrackerHandler(subscriptions_list)
eyetracker.subscribe()
time.sleep(2)
eyetracker.unsubscribe()

""" Save eye images and gaze data to json files. """
# eyetracker.write_files()
# write_file('datafiles/gaze_data.json', data=all_gaze_data)
# write_file('datafiles/eye_images.pkl', data=all_eye_images)

# %%
# 'Import' code (pull in code that tobii etc. have written so we can use it)
import json
import time
import numpy as np
import tobii_research as tr
from tobiiresearch.implementation.EyeTracker import EyeTracker, find_all_eyetrackers
from helpers import save_eye_images_as_png, write_file

# %%
def subscribe():
    def gaze_data_callback(gaze_data):
        """ Function that will be 'passed on' to the eytracker to tell it what to do at each sample (currently just adds all data to the list)"""
        all_gaze_data.append(gaze_data)
    
    def eye_images_callback(eye_image):
        """ Function that will be 'passed on' to the eytracker to tell it what to do at each sample (currently just adds all data to the list)"""
        all_eye_images.append(eye_image)

    # Subscribe to the eyetracker (start sampling data)
    eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)  # begin subscribing
    eyetracker.subscribe_to(tr.EYETRACKER_EYE_IMAGES, eye_images_callback, as_dictionary=True)  # begin subscribing

def unsubscribe():
    """ Function to STOP sampling data... can run it by writing 'unsubscribe()'. """
    eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA)
    eyetracker.unsubscribe_from(tr.EYETRACKER_EYE_IMAGES)

# Define the empty list of data which we will add to in the file
all_gaze_data = []
all_eye_images = []

# Set up the eyetracker initially by calling setup_eyetracker
def setup_eyetracker() -> EyeTracker | None:
    """ Setup function that will 'find' the eyetracker if it exists (is plugged into the PC)"""
    all_trackers = find_all_eyetrackers()
    return(all_trackers[0])

# Setup eyetracker, record for 2s, then sleep
eyetracker = setup_eyetracker()
subscribe()
time.sleep(2)
unsubscribe()

# %%
""" Save eye images and gaze data to json files. """
write_file(all_gaze_data, 'datafiles/gaze_data.json')
write_file(all_eye_images, 'datafiles/eye_images.pkl')

# %%





# %%
# EXAMPLE DATA FOR ONE TIME POINT (will be sammpled 250 times per second)
"""
 {'device_time_stamp': 813349118,
  'system_time_stamp': 523967055208,

  'left_gaze_point_on_display_area': (0.24509266018867493, 1.1494059562683105),
  'left_gaze_point_in_user_coordinate_system': (-88.07263946533203,
   -22.229705810546875,
   -18.73270606994629),

  'left_gaze_point_validity': 1,
  'left_pupil_diameter': 4.982452392578125,
  'left_pupil_validity': 1,
  'left_gaze_origin_in_user_coordinate_system': (-175.59963989257812,
   39.657161712646484,
   556.5618896484375),
  'left_gaze_origin_in_trackbox_coordinate_system': (0.929452657699585,
   0.4033617377281189,
   0.30945754051208496),
  'left_gaze_origin_validity': 1,

  'right_gaze_point_on_display_area': (0.02701735310256481,
   1.2251988649368286),
  'right_gaze_point_in_user_coordinate_system': (-163.49655151367188,
   -37.625328063964844,
   -24.336275100708008),
  'right_gaze_point_validity': 1,
  'right_pupil_diameter': 5.9588775634765625,
  'right_pupil_validity': 1,
  'right_gaze_origin_in_user_coordinate_system': (-117.00442504882812,
   39.52165985107422,
   571.5350341796875),
  'right_gaze_origin_in_trackbox_coordinate_system': (0.7810330390930176,
   0.40643832087516785,
   0.3093472719192505),
  'right_gaze_origin_validity': 1},"""
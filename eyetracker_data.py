# %%
""" File to process saved eyetracker pkl data. """

from helpers import read_file
import matplotlib.pyplot as plt

gaze_data = read_file('datafiles/1719942762/eyetracker_gaze_data.pkl')
valid_list = [timestamp['left_pupil_validity'] == 1 or timestamp['right_pupil_validity'] == 1 for timestamp in gaze_data]

plt.plot(valid_list)


# %% 
import time
from tobiiresearch.implementation.EyeTracker import EyeTracker, find_all_eyetrackers

from . import write_file

class EyetrackerHandler():
    """
    Handler class for the eyetracker.

    Args:
        subscriptions_list (list): List of subscriptions to record.
        parent_folder (str, optional): Parent folder to save data in. Defaults to 'datafiles'.
        individual_folder (str, optional): Individual folder to save data in. Defaults to None.
    """
    def __init__(self, subscriptions_list: list, parent_folder: str = 'datafiles', individual_folder: str = None):
        # Default to current timestamp in seconds
        if individual_folder is None: individual_folder = str(int(time.time()))

        self.parent_folder, self.individual_folder = parent_folder, individual_folder
        self.eyetracker = self.setup_eyetracker()
        self.subscriptions_list = subscriptions_list
        self.data_dict = {subscription_name: [] for subscription_name in subscriptions_list}

    def setup_eyetracker(self) -> EyeTracker | None:
        """
        Setup function that will 'find' the eyetracker if it exists (is plugged into the PC).

        Returns:
            EyeTracker: The found eyetracker.
        """
        all_trackers = find_all_eyetrackers()
        if len(all_trackers) == 0: raise ValueError('No eyetrackers found!')
        return(all_trackers[0])

    def subscribe(self) -> None:
        """ Subscribe to the given subscriptions. """
        for subscription_name in self.subscriptions_list:
            self.eyetracker.subscribe_to(subscription_name, self.data_dict[subscription_name].append, as_dictionary=True)

    def unsubscribe(self):
        """ Unsubscribe from the given subscriptions. """
        for subscription_name in self.subscriptions_list:
            self.eyetracker.unsubscribe_from(subscription_name)

    def write_files(self):
        """ Write the recorded data as pickle files in the selected folder. """
        for subscription_name, data in self.data_dict.items():
            write_file(f'{self.parent_folder}/{self.individual_folder}/{subscription_name}.pkl', data=data)
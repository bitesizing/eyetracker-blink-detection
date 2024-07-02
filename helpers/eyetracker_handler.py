from tobiiresearch.implementation.EyeTracker import EyeTracker, find_all_eyetrackers

class EyetrackerHandler():
    def __init__(self, subscriptions_list: list):
        self.eyetracker = self.setup_eyetracker()
        self.subscriptions_list = subscriptions_list
        self.data_list = [{subscription_name: []} for subscription_name in subscriptions_list]

    def setup_eyetracker() -> EyeTracker | None:
        """ Setup function that will 'find' the eyetracker if it exists (is plugged into the PC)"""
        all_trackers = find_all_eyetrackers()
        return(all_trackers[0])

    def subscribe(self):
        for subscription_name in self.subscriptions_list:
            self.eyetracker.subscribe_to(subscription_name, self.data_list[-1][subscription_name].append, as_dictionary=True)

    def unsubscribe(self):
        for subscription_name in self.subscriptions_list:
            self.eyetracker.unsubscribe_from(subscription_name)
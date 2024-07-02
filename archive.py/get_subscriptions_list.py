# %%
import tobii_research as tr

with open('subscriptions_list.txt', 'r') as f:
    subscriptions_list = f.read().split(", ")

parsed_subscriptions_list = []
for subscription_name in subscriptions_list:
    if hasattr(tr, subscription_name):
        parsed_subscriptions_list.append(getattr(tr, subscription_name))

with open("subscriptions_list_parsed.txt", "w") as f:
    f.write("\n".join(parsed_subscriptions_list))
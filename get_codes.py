from tweety import Twitter
import os
from dotenv import load_dotenv
from tweety.filters import SearchFilters
import re
import time

load_dotenv()
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
app = Twitter("session")
app.sign_in(username, password)

codes = []
# pattern to find in tweet text
pattern = r'bsky-social-[a-zA-Z0-9]+-[a-zA-Z0-9]+'


print("Here are the bluesky codes found  (will be updated every 30s):")
while (True):
    # can't remove bsky.social.* username from searches :(
    tweets = app.search("'bsky-social-'", filter_=SearchFilters.Latest())
    for tweet in tweets:
        matches = re.findall(pattern, tweet.text)
        for match in matches:
            if (match not in codes):
                print(match)
                codes.append(match)
    time.sleep(30)

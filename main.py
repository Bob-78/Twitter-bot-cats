# main.py

import image
import tweet
import follow
import time
from definitions import base_url

	
while True:
    
    # try to get image
    try:
        image.get_image(base_url)
    except:
        pass
    
    # try to post tweet
    try:
        tweet.post()     
    except:
        pass
    
    # unfollow some non_friends
    try:
        unfollow_non_friends(5)
    except:
        pass
    
    # try to follow x people who've tweeted with hashtag
    try:
        follow.now(1)
    except:
        pass
    
    print("waiting before next cycle")
    time.sleep(1800) #Tweet every 30 minutes
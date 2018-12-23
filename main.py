# main.py

import image
import tweet
import follow
import time
from definitions import base_url

	
while True:
    
    # try to get image
    try:
        print("main: trying to get image")
        image.get_image(base_url)
    except:
        print("main: could not get image")
        pass
    
    # try to post tweet
    try:
        print("main: trying to post tweet")
        tweet.post()     
    except:
        print("main: could not post tweet")
        pass
    
    # unfollow some non_friends
    try:
        print("main: trying to unfollow non-friends")
        unfollow_non_friends(5)
    except:
        print("main: could not unfollow non-friend")
        pass
    
    # try to follow x people who've tweeted with hashtag
    try:
        print("main: trying to follow")
        follow.now(1)
    except:
        print("main: could not follow new id")
        pass
    
    print("waiting before next cycle")
    time.sleep(1800) #Tweet every 30 minutes
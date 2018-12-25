# main.py

import image
import tweet
import follow
import time
import definitions

	
while True:
    
    # try to get image
    try:
        print("main: trying to get image")
        image.get_image()
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
        
    # try to follow x people who've tweeted with hashtag
    try:
        print("main: trying to follow")
        follow.now(definitions.people_to_follow)
    except:
        print("main: could not follow new id")
        pass
    
    #Wait to not overload the Twitter API
    print("main: waiting {} seconds".format(definitions.sleep_time))
    time.sleep(definitions.sleep_time) 
    
    # unfollow some non_friends    
    try:
        print("main: trying to unfollow non-friends")
        follow.unfollow_non_friends(definitions.non_friends_to_unfollow)
    except:
        print("main: could not unfollow non-friend")
        pass

    #Wait 15 min to not overload the Twitter API
    print("main: waiting {} seconds".format(definitions.sleep_time))
    time.sleep(definitions.sleep_time) 
    
    print("main: OK, done. Going to next cycle.")

# post_tweet

import api
import helpers
from definitions import message_hashtags, messages


def get_message():
    while True:
   
        # get two random messages 
        text1 = messages[helpers.random_list_number(messages)] # get random message from the messages
        text2 = messages[helpers.random_list_number(messages)] # get random message from the messages
    
        # if the texts are the same, try again
        if text1 == text2:
        
            continue
    
        else: 
            
            # return the two strings
            return str(text1 + " " + text2)

def post():
    print("...function post_tweet called")
    
    # create the api
    my_api = api.make_api()

    #define the file name    
    filename = "temp_image.jpg"
    
    # define the message
    message = get_message()
                
    # send the tweet with the image and a random message
    my_api.update_with_media(filename, status = message + message_hashtags)
    print("tweeted!")
    print("...")

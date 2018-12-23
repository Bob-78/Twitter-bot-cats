# helpers.py

import urllib.request
from bs4 import BeautifulSoup
from random import randint


# helper function to get soup form a url
def get_soup(soup_url):
        
    print("...function get_soup called")

    # requesting the html
    html = urllib.request.urlopen(soup_url)

    # parse the html using beautiful soup and store in variable
    soup = BeautifulSoup(html,"html.parser")
    
    print("returning soup")

    return soup

        
# helper function to get a random list number
def random_list_number(list_name):
        
    print("...function random_list_number called") 
    
    random_list_number = randint(0, len(list_name)-1)
    
    return random_list_number 
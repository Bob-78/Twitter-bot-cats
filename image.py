# image.py

import urllib.request
from random import randint
from bs4 import BeautifulSoup
import helpers
from definitions import base_url

def get_image(base_url):

    print("function get_image called")

    # gets the total number of pages
    def get_total_pages(base_url):
    
        print("...function total_pages called")

        # get some soup for our url
        soup = helpers.get_soup(base_url + "1")

        total_pages = soup.find('form', {'class': 'add_search_params pure-form hide-xs hide-sm hide-md'}).getText()
        total_pages = [int(s) for s in total_pages.split() if s.isdigit()][0]

        print("...returning total pages: {}".format(total_pages))
    
        return total_pages
    

    # select a random page from the total pages
    def get_random_page_url(base_url):
    
        print("...function get_random_page_url called")
    
        total_pages = get_total_pages(base_url)

        # create random number within range of total pages
        random_page_number = randint(1, total_pages)

        # append random number to the base url
        random_page_url = base_url + str(random_page_number)

        print("...returning url: {}".format(random_page_url))

        return random_page_url


    # gets all the image urls from a page
    def get_image_url(page_url):
    
        print("...function get_image_url called")
    
        #get the soup
        soup = helpers.get_soup(page_url)

        # make list of all the image urls
        links = [element['data-lazy-srcset'] for element in soup.findAll('img', attrs = {'data-lazy-srcset' : True})]
        
        # select a random url from the list of links
        image_url = links[helpers.random_list_number(links)]

        # do some cleanup
        image_url = image_url.split(',')[1] # split list elements, keep only the second one ([1]), the 480p one
        image_url = image_url.split(' ')[1]  # split list elements, keep only the first one ([0]), drop the 2x
        image_url = image_url.replace("_480", "1280") # get the larger size images

        print("...Using this url: {}".format(image_url))
    
        return image_url

    def download_image(base_url):

        print("...function download_image called")

        # get the page url
        page_url = get_random_page_url(base_url)
    
        # get the image url
        image_url = get_image_url(page_url)
    
        # download the image 
        filename ="temp_image.jpg"
        urllib.request.urlretrieve(image_url, filename)

        print("...image temp_image.jpg saved")


    # call the download image function
    download_image(base_url) 
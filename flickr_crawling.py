import urllib.request
import requests
import json

from bs4 import BeautifulSoup


city_adjective = open('data/city.txt', 'r')
base_url = 'https://www.flickr.com/search/?text={}%20city'

#processing adjective file
for line in city_adjective.readlines():
    splitted_line = line.strip().split('_')
    splitted_line = splitted_line[0].split('-')
    if len(splitted_line) == 1:
        url = base_url.format(splitted_line[0])
        print (url)
    elif len(splitted_line) == 2:
        url = base_url.format('{}%20{}'.format(splitted_line[0], splitted_line[1]))
        print (url)
    else:
        print ("Exception: {}").format(line)

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    photo_url = soup.find_all('div', attrs={'class':"view photo-list-photo-view awake"})

    #photo_url = soup.find_all('a', attrs={'href':'/photos/artiephotography/12809954313/'})
    print (photo_url)

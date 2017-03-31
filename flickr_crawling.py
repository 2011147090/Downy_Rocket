import requests
import json
import sys
from bs4 import BeautifulSoup

city_adjective = open('data/city.txt', 'r')
base_url = 'https://www.flickr.com/search/?text={}%20city'

#processing adjective file
for line in city_adjective.readlines():
    splitted_line = line.strip().split('_')
    splitted_line = splitted_line[0].split('-')
    if len(splitted_line) == 1:
        url = base_url.format(splitted_line[0])
        #print (url)
    elif len(splitted_line) == 2:
        url = base_url.format('{}%20{}'.format(splitted_line[0], splitted_line[1]))
        #print (url)
    else:
        print ("Exception: {}").format(line)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    photo_urls = soup.find_all('div', attrs={'class': "view photo-list-photo-view requiredToShowOnServer awake"})
    print (line)
    for photo_url in photo_urls:
        base_photo_url = "c1.staticflickr.com{}.jpg"
        parsed_url = str(photo_url).split('c1.staticflickr.com')[1].split('.jpg')[0]
        photo = base_photo_url.format(parsed_url)
        print (photo)
    print ("-"*70)
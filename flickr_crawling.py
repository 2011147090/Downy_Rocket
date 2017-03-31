import requests
import json
from bs4 import BeautifulSoup

city_adjective = open('data/city.txt', 'r')
base_url = 'https://www.flickr.com/search/?text={}%20city'

dict = {}

#processing adjective file
for line in city_adjective.readlines():
    splitted_line = line.strip().split('_')
    noun = splitted_line[-1].strip()
    adjective_list = []
    adjective_list = splitted_line[0].split('-')
    if len(adjective_list) == 1:
        url = base_url.format(adjective_list[0])
        #print (url)
    elif len(adjective_list) == 2:
        url = base_url.format('{}%20{}'.format(adjective_list[0], adjective_list[1]))
        #print (url)
    else:
        print ("Exception: {}").format(line)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    photo_urls = soup.find_all('div', attrs={'class': "view photo-list-photo-view requiredToShowOnServer awake"})
    print (line.strip())
    for i, photo_url in enumerate(photo_urls):
        photo_id = "{}_{}".format(line.strip().replace('-','_'), i)
        base_photo_url = "c1.staticflickr.com{}.jpg"
        parsed_url = str(photo_url).split('c1.staticflickr.com')[1].split('.jpg')[0]
        photo = base_photo_url.format(parsed_url)
        if noun in dict.keys():
            dict[noun].update({photo_id : {'id': photo_id, 'url':photo, 'adjective':adjective_list, 'noun':noun, 'path':'dataset/{}'.format(photo_id)}})
        else:
            dict[noun] = {photo_id: {'id': photo_id, 'url': photo, 'adjective': adjective_list, 'noun': noun, 'path':'dataset/{}'.format(photo_id)}}
        #print (photo)
    #print ("-"*70)

with open('photo_profile.json', 'w') as write_json:
    json.dump(dict, write_json)
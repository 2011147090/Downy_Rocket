import flickrapi

api_key = '5368a00d3ea7a66c2e3e38c624cac5f9'
api_secret = '79b370b1c36b3b65'

flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')

# ----------------------------------------------------------------------

f = open('city.txt', 'r')
lines = f.readlines()
f.close()

# ----------------------------------------------------------------------

for line in lines:
    my_tag = line[:-7] + ', city'

    try:
        srch = flickr.photos.search(tags=my_tag, tag_mode='all', per_page=500)
        print (my_tag, len(srch['photos']['photo']))
    except:
        continue

    # for i in srch['photos']['photo']:
    #     try:
    #         urls = flickr.photos.getSizes(photo_id=i['id'])
    #     except:
    #         continue
    #
    #     print (urls['sizes']['size'][1]['source'])

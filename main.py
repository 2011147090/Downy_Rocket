import flickrapi

api_key = '5368a00d3ea7a66c2e3e38c624cac5f9'
api_secret = '79b370b1c36b3b65'

flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')

# ----------------------------------------------------------------------
my_tag = 'disgusting, baby'
# ----------------------------------------------------------------------


srch = flickr.photos.search(tags=my_tag, tag_mode='all', text=my_tag, safe_search=3, sort='relevance', page=2)
for i in srch['photos']['photo']:
    try:
        urls = flickr.photos.getSizes(photo_id=i['id'])
    except:
        continue
    try:
        print urls['sizes']['size'][4]['source']
    except:
        continue

    # for i in urls['sizes']['size']:
    #     print i
    #
    # print ''



# clus = flickr.tags.getClusters(tag=my_tag)
# for i in clus['clusters']['cluster']:
#     print i


# rela = flickr.tags.getRelated(tag=my_tag)
# for i in rela['tags']['tag']:
#     print i


# tags = flickr.tags.getClusterPhotos(tag=my_tag)
# for i in tags[u'photos'][u'photo']:
#     try:
#         urls = flickr.photos.getSizes(photo_id=i['id'])
#     except:
#         continue
#
#     print urls['sizes']['size'][-1]['source']

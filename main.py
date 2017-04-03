import urllib.request

photo_profile = open("./photo_profile.json", "r")

while True:

    line = photo_profile.readline()
    if not line:
        break

    path_pos = line.find("path")
    if path_pos != -1:
        path_line = line
        path = path_line[path_pos + 8:-3]

    url_pos = line.find("url")
    if url_pos != -1:
        url_line = line

        url = url_line[url_pos + 7:-3]
        real_url = "http://{}".format(url)

        req = urllib.request.Request(real_url)
        data = urllib.request.urlopen(req).read()

        f = open(path, "wb")
        f.write(data)
        f.close()
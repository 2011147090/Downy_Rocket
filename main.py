import urllib.request

url = "c1.staticflickr.com/7/6230/6311964008_946f87324f_m.jpg"
real_url = "http://{}".format(url)

req = urllib.request.Request(url)
data = urllib.request.urlopen(req).read()

f = open("./image.jpg", "wb")
f.write(data)
f.close()
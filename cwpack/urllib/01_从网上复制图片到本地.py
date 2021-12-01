import urllib.request
import os
os.chdir(os.path.split(os.path.realpath(__file__))[0])


response = urllib.request.urlopen("http://placekitten.com/g/200/300")
cat_img = response.read()
with open("cat.jpg", "wb") as f:
    f.write(cat_img)


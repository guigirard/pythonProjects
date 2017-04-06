import requests
'''
from io import BytesIO
from PIL import Image

r = requests.get("http://wallpaper-gallery.net/images/wallpaper-png/wallpaper-png-10.jpg")

print("Status code:", r.status_code)

image = Image.open(BytesIO(r.content))

path = "./image." + image.format

print(image.size, image.format, image.mode)

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save image.")

# -------------------------------------------------------------------
my_data = {"name": "Guillaume", "email": "guillaume@example.co"}

r = requests.post("https://www.w3schools.com/php/welcome.php", data=my_data)

f = open("myfile.html", "w+")
f.write(r.text)
'''

# --------------------------------------------------------------------
import simplejson as json

url = "https://www.googleapis.com/urlshortener/v1/url"
payload = {"longUrl": "http://example.com"}
headers = {"Content-Type": "application/json"}
r = requests.post(url, json=payload, headers=headers)

print(r.headers)

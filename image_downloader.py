import random
import urllib.re

def download_web_image(url):
	name = random.randrange(1,1000)
	fullname = str(name) + ".jpg"
	urllib.urlretrieve(url,fullname)

download_web_image("https://www.instagram.com/p/BOkLEZuAnre/")
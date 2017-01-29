import urllib
import bs4 as bs
import random
import json

sauce = urllib.urlopen("https://www.just-eat.ca/area/h3a-montreal/").read()
soup = bs.BeautifulSoup(sauce,"lxml")

res = random.sample(soup.find_all("h3"),1)

info = {"name":res[0].text}

addr = res[0].parent.parent.find_all("p",itemprop="address")
info["address"] = addr[0].text

link = res[0].parent.parent.parent.parent.parent.parent.find_all("a",{'class':"mediaElement listing-item-link"})
web = "https://www.just-eat.ca"+link[0]['href']
info["website"] = web

print json.dumps(info)
import urllib
import bs4 as bs
import random
import json

jsonArr=[]
def repeat():
	for x in range(0,100):
		sauce = urllib.urlopen("https://www.just-eat.ca/area/h3a-montreal/").read()
		soup = bs.BeautifulSoup(sauce,"html.parser")
		
		num = random.randint(0, len(soup.find_all("h3"))-1)
		res = soup.find_all("h3")[num]

		info = {"name":res.text}

		addr = res.parent.parent.find_all("p",itemprop="address")
		info["address"] = addr[0].text

		link = res.parent.parent.parent.parent.parent.parent.find_all("a",{'class':"mediaElement listing-item-link"})
		web = "https://www.just-eat.ca"+link[0]['href']
		info["website"] = web

		print json.dumps(info)

		jsonArr.extend([json.dumps(info)])

	return jsonArr


repeat()
Json = {'restaurant': jsonArr}

f = open('restaurant.json', 'a')
f.write(json.dumps(Json))
f.write('\n')
f.close

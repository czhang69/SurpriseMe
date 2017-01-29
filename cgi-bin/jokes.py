import urllib
import bs4 as bs
import re
from random import randint
import json

jsonArr=[]

def repeat():
	for x in range(0,100):
		url="http://worldsfunniestjokes.club/top-50-funniest-jokes-in-the-world/"

		subcontent = urllib.urlopen(url).read()
		subsoup=bs.BeautifulSoup(subcontent,'html.parser')
		theBody=re.findall(re.compile("<br(.*?)</p>",re.DOTALL),str(subsoup))

		randomInt=randint(1,len(theBody)-1)
		s=theBody[randomInt][3:]
		while "<" in s:
		    randomInt = randint(1, len(theBody) - 1)
		    s = theBody[randomInt][3:]
		Joke={'joke':s}

		print(json.dumps(Joke))

		jsonArr.extend([json.dumps(Joke)])
		
	return jsonArr

repeat()
Json = {'jokes': jsonArr}

f = open('jokes.json', 'a')
f.write(json.dumps(Json))
f.write('\n')
f.close



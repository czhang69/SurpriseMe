import urllib.request
import urllib.parse
import bs4 as bs
import re
from random import randint


url="http://worldsfunniestjokes.club/top-50-funniest-jokes-in-the-world/"

subcontent = urllib.request.urlopen(url).read()
subsoup=bs.BeautifulSoup(subcontent,'html.parser')
theBody=re.findall(re.compile("<br(.*?)</p>",re.DOTALL),str(subsoup))

randomInt=randint(1,len(theBody)-1)
s=theBody[randomInt][3:]
Joke={
    'joke':s
}

import json
print(json.dumps(Joke))


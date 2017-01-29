import urllib.request
import urllib.parse
import bs4 as bs
import re
from random import randint

num=randint(1,3)
webs={
    1:"http://www.forbes.com/sites/kevinkruse/2013/05/28/inspirational-quotes/#709da5cc6697",
    2:"http://www.forbes.com/sites/kevinkruse/2013/05/28/inspirational-quotes/2/#77bade934c37",
    3:"http://www.forbes.com/sites/kevinkruse/2013/05/28/inspirational-quotes/3/#74bb475b4e82"
}
url=webs[3]

subcontent = urllib.request.urlopen(url).read()
subsoup=bs.BeautifulSoup(subcontent,'html.parser')
theBody=re.findall(re.compile("<p>[0-9](.*?)</p>",re.DOTALL),str(subsoup))
randomInt=randint(1,len(theBody)-1)
s=theBody[randomInt][3:]
Quote={
    'quote':s
}

import json
print(json.dumps(Quote))

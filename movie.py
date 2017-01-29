import urllib.request

import bs4 as bs
import re
from random import randint
import json

jsonArr = []
def repeat():
    for x in range (0,100):

        listName=['action','animation','comedy','documentary','family','film_noir','horror','musical','romance','sport','war','adventure','biography','crime','drama','fantasy','history','music','mystery','sci_fi','thriller','western']

        genre=listName[randint(0,len(listName)-1)]
        mainUrl="http://www.imdb.com/genre/"+genre+"/?ref_=gnr_mn_ac_mp"
        sauce = urllib.request.urlopen(mainUrl).read()
        soup=bs.BeautifulSoup(sauce,'html.parser')
        paragraphs=re.findall("<a href=\"/title/tt......./\">(.*?)</a>",str(soup))

        randomInt=randint(0,len(paragraphs)-1)

        target=paragraphs[randomInt]
        title=target
        refind=re.findall("<a href=\""+"(.*?)"+"\">"+target+"</a>",str(soup))
        if not refind:
            continue
        url="http://www.imdb.com/"+refind[0]+"plotsummary?ref_=tt_stry_pl"

        subcontent = urllib.request.urlopen(url).read()
        subsoup=bs.BeautifulSoup(subcontent,'html.parser')
        theBody=re.findall(re.compile("<p class=\"plotSummary\">(.*?)</p>",re.DOTALL),str(subsoup))
        if not theBody:
            continue
        result=theBody[0]
        print(url)

        imgSrc=''
        for img in subsoup.find_all('img'):
            if(img.get('itemprop')=='image'):
                 imgSrc=img.get('src')

        movie={
            'title':title,
            'description':result[1:],
            'image':imgSrc,
            'url':url
        }

        jsonArr.extend([json.dumps(movie)])
    return jsonArr

repeat()
Json = {'movie': jsonArr}

f = open('movie.json', 'a')
f.write(json.dumps(Json))
f.write('\n')
f.close

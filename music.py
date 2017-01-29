import urllib.request
from bs4 import BeautifulSoup
import random
import json

source = urllib.request.urlopen("https://www.youtube.com/music").read()
soup=BeautifulSoup(source,'html.parser')

temp = soup.find_all('div',{'class': 'yt-lockup-content'})
randomNum = random.randint(0,len(temp)-1)
temp1=temp[randomNum].find_all('h3',{'class': 'yt-lockup-title'})[0].getText('title')
suburl=temp[randomNum].find('a')['href']

index = int(temp1.index('title - Duration'))
music = temp1[0:index]
print (music)

url = 'https://www.youtube.com' + suburl
print (url)

source1 = urllib.request.urlopen(url).read()
soup1=BeautifulSoup(source1,'html.parser')
views = soup1.find_all('div',{'class': 'watch-view-count'})

v=str(views)
numOfViews = v[31:-13]
print(numOfViews)

image = "https://lh3.googleusercontent.com/-E-jAfuwURMbYgvRhS8xLL8p280U9ueeC-IDrJOFmxGZpBJCWOY4jTbOKK1DZkPIFAUu=w300"

musicInfo={}
musicInfo['recomand']={
    'music':music,
    'number of views':numOfViews,
    'url':url,
    'image': image
}

print(json.dumps(musicInfo))



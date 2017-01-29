from bs4 import BeautifulSoup
import urllib
import random
import re
import json

category = ['art', 'biography', 'business', 'chick-lit', 'children-s', 'christian', 'classics', 'comics', 'contemporary', 'cookbooks',
			'crime', 'fantasy', 'fiction', 'gay-and-lesbian', 'graphic-novels', 'historical-fiction', 'history', 'horror', 'humor-and-comedy',
			'manga', 'memoir', 'music', 'mystery', 'nonfiction', 'paranormal', 'philosophy', 'poetry', 'psychology', 'religion',
			'romance', 'science', 'science-fiction', 'self-help', 'suspense', 'spirituality', 'sports', 'thriller', 'travel']

jsonArr=[]
def repeat():
	for x in range(0,5):
		url = "https://www.goodreads.com/genres/" + random.choice(category)

		source = urllib.urlopen(url).read()
		soup = BeautifulSoup(source,'html.parser')

		temp = soup.findAll('div', {'class': 'coverWrapper'})
		randomNum = random.randint(0, len(temp)-1)

		'Get Book Name && Book Cover'
		oneDiv = temp[randomNum].findAll('img')[0]
		title = oneDiv.get('alt')
		imgLink = oneDiv.get('src')

		'Get Book ID'
		bookURL = "https://www.goodreads.com/" + temp[randomNum].findAll('a')[0].get('href')

		subSource = urllib.urlopen(bookURL).read()
		subSoup = BeautifulSoup(subSource, 'html.parser')

		for bookId in subSoup.findAll('a'):
			if bookId.get('data-text-id') != None:
				break

		bookId = "freeTextContainer" + bookId.get('data-text-id').encode('ascii', 'ignore')

		description = subSoup.findAll('span', {'id': bookId})[0].text

		final = {"title": title}
		final["image"] = imgLink
		final["url"] = bookURL
		final["description"] = description


		print json.dumps(final)
		jsonArr.extend([json.dumps(final)])

	return jsonArr

repeat()
Json = {'books': jsonArr}

f = open('books.json', 'a')
f.write(json.dumps(Json))
f.write('\n')
f.close
















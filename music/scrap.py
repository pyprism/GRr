from bs4 import BeautifulSoup
from urllib2 import urlopen

url = "http://www.music.com.bd/download/browse/M/Moushumi/"


html = urlopen(url).read()
soup = BeautifulSoup(html)

#print soup.find_all("a", class_='autoindex_a')[0]

"""
url = "http://www.music.com.bd/download/browse/"
#front page
x = soup.find_all("a", class_='autoindex_a')

hiren = 0

for i in x:
	print i.get('href')
	hiren = hiren + 1
	print hiren
"""

"""
x = soup.find_all("a", class_='autoindex_a')
for i in x:
	print i.get('href')

"""

def alphaSelect():
	url = "http://www.music.com.bd/download/browse/"
	html = urlopen(url).read()
	soup = BeautifulSoup(html)
	x = soup.find_all("a", class_='autoindex_a')
	return x

def 
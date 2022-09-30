from bs4 import BeautifulSoup as BS
import requests
import lxml

url = 'https://ami.by/catalog/sofabeds.html'

item_dict = dict()

def pars(url):
	global items_dict
	html = requests.get(url).text
	soup = BS(html, 'lxml')
	item_cont = soup.find('div', class_ = 'itemsgrid') 
	for index in item_cont.find_all('div', class_ = 'item'):
		name = index.find('div', class_ = 'itemtitle').find('a').text
		price_now = int(index.find('div', class_ = 'Price').find('span', class_ = 'digitsGroup2').text)
		item_dict[name] = price_now

if __name__ == '__main__':
	pars(url)
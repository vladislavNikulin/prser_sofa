from bs4 import BeautifulSoup as BS
import requests
import lxml

import sqlite3

url = 'https://ami.by/catalog/sofabeds.html'

item_dict = dict()
sofa_list = list()

def pars(url):
	global items_dict, sofa_list
	html = requests.get(url).text
	soup = BS(html, 'lxml')
	item_cont = soup.find('div', class_ = 'itemsgrid') 
	for index in item_cont.find_all('div', class_ = 'item'):
		name = index.find('div', class_ = 'itemtitle').find('a').text
		price_now = int(index.find('div', class_ = 'Price').find('span', class_ = 'digitsGroup2').text)
		sofa_list.append(name)
		item_dict[name] = price_now

def create_tb():
	global sql, cur
	sql = sqlite3.connect('datebase.db')
	cur = sql.cursor()
	cur.execute('CREATE TABLE IF NOT EXISTS sofas(name TEXT, price INT)')
	sql.commit()

def add_to_table():
	for index in range(len(item_dict)):
		name = sofa_list[index]
		price = item_dict.get(sofa_list[index])
		cur.execute('INSERT INTO sofas VALUES(?,?)', (name, price))
		sql.commit()

if __name__ == '__main__':
	pars(url)
	create_tb()
	add_to_table()
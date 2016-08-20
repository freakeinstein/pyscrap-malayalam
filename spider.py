#! /usr/bin/env python3

import requests as re
import regex as rx
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse
from urllib.parse import urljoin
import rules

url_list_unex, url_list_ex = [],[]
page_counter, max_pages = 0,10

start_url = 'http://www.absarmohamed.com/2016/08/zakirnaik.html'
base_url = 'http://www.absarmohamed.com' # only web pages with this base url will be explored.


def load_source(url):
	response = re.get(url)
	try:
		response = re.get(url, timeout=10)
		response.raise_for_status()
	except Exception:
		return ''
	return response


def soup_cup(source_text):
	soup = bs(source_text,'lxml')

	all_links = soup.findAll('a',href = True)
	pluck_all_links(all_links)

	text = rules.old_blogger(soup) ##############################  APPLY RULE HERE !! #########################
	print(text,"\n")


def run_spider(url):
	source = load_source(url)
	# we need to pass plain source text to beautiful soup
	plain_text = source.text
	soup_cup(plain_text)


def pluck_all_links(links):
	for url in links:
		url = url['href']
		if url.startswith('/'):
			url = urljoin(base_url,url)
		if same_url_base(url,base_url):
			url_list_unex.append(url)


def same_url_base(url1,url2):
	o1 = urlparse(url1)
	o2 = urlparse(url2)
	if o1.netloc == o2.netloc:
		return True
	else:
		return False




if __name__ == '__main__':
	
	url_list_unex.append(start_url)

	for url in url_list_unex:
		#print(url)
		if url not in url_list_ex:
			page_counter += 1
			run_spider(url)
			url_list_ex.append(url)

			print(page_counter)
			if page_counter > max_pages:
				break
		url_list_unex.remove(url)
	#print(url_list_unex)















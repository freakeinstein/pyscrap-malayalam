#! /usr/bin/env python3


import regex as rx


def mathrubhoomi(soup):
	text = ""
	for articles in soup.findAll('div',{ 'id' : 'article' }):
		for str in articles.findAll('h1'):
			if str.string is not None:
				text += str.string
		for str in articles.findAll('p'):
			if str.string is not None:
				text += str.string
		text = rx.sub( '\s+', ' ', text ).strip()
	return text

def manorama(soup):
	text = ""
	for articles in soup.findAll('div',{ 'class' : 'article' }):
		for str in articles.findAll('h1'):
			if str.string is not None:
				text += str.string
		for str in articles.findAll('p'):
			if str.string is not None:
				text += str.string
		text = rx.sub( '\s+', ' ', text ).strip()
	return text

def mangalam(soup):
	text = ""
	for articles in soup.findAll('div',{ 'class' : 'article' }):
		for str in articles.findAll('h1'):
			if str.string is not None:
				text += str.string
		for str in articles.findAll('p'):
			if str.string is not None:
				text += str.string
		text = rx.sub( '\s+', ' ', text ).strip()
	return text

def deshabhimani(soup):
	text = ""
	for articles in soup.findAll('div',{ 'class' : 'story' }):
		for str in articles.findAll('h1'):
			if str.string is not None:
				text += str.string
		for str in articles.findAll('p'):
			if str.string is not None:
				text += str.string
		text = rx.sub( '\s+', ' ', text ).strip()
	return text

def old_blogger(soup):
	text = ""
	for articles in soup.findAll('div',{ 'dir' : 'ltr' }):
		for str in articles.findAll('div'):
			if str.string is not None:
				text += str.string
		text = rx.sub( '\s+', ' ', text ).strip()
	return text





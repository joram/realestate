import os
import urllib
import userAgent
import time
from BeautifulSoup import BeautifulSoup          # For processing HTML
from urllib import FancyURLopener
import datetime
from datetime import datetime

class suttonDetails():
	def domain(self):
		return "sutton"

	indexBaseURL = "http://www.sutton.com"

	def allInfoLinks(self, content):
		links = []
		soup = BeautifulSoup(content)
		linkData = soup.findAll('a')
		for link in linkData:
			if link.has_key('href') and "/listings/view/" in link['href']:
				links.append(link['href'])
		links = list(set(links))
		return links

	def indexURL(self,page):
		return self.indexBaseURL+"/listings/BC/Victoria?page=0%2C"+str(page)	

	def mlsFromPosting(self,content):
		soup = BeautifulSoup(content)
		mls = soup.find('div', {"id":"mls"}).contents	
		if mls:
			return str(mls).replace("MLS: ","")
		return "no_mls"

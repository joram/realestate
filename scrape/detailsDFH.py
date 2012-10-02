import os
import urllib
import userAgent
import time
from BeautifulSoup import BeautifulSoup          # For processing HTML
from urllib import FancyURLopener
import datetime
from datetime import datetime

class dfhDetails():
	indexBaseURL = "http://dfh.ca/"
	def domain(self):
		return "dfh"

	def indexURL(self,page):
		return "http://dfh.ca/featured_listings.html?custom=Y&orderby=mls&sales=N&agency_id=2&%20page="+str(page)
	
	def allInfoLinks(self, content):
		links = []
		soup = BeautifulSoup(content)
		linkData = soup.findAll('a')
		for link in linkData:
			if link.text=="More info" and link.has_key('href'):
				links.append(link['href'])
		return links

	def mlsFromPosting(self,content):
		soup = BeautifulSoup(content)
                fonts = soup.findAll('font', {"size":"2"})

		mls = "no_mls"
		for font in fonts:
			try:
				integer = int(font.text.replace('VI',''))
				mls = font.text.replace(' VI','_VI')
			except:
				if mls=="no_mls":
					mls="no_mls"	
		return mls


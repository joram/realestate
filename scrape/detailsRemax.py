import os
import urllib
import userAgent
import time
from BeautifulSoup import BeautifulSoup          # For processing HTML
from urllib import FancyURLopener
import datetime
from datetime import datetime

class remaxDetails():
	def domain(self):
		return "remax"

	indexBaseURL = "http://camosun.britishcolumbia.remax.ca/listings/"

	def allInfoLinks(self, content):
		links = []
		soup = BeautifulSoup(content)
		linkData = soup.findAll('a', {'title':"click here to view details"} )
		for link in linkData:
			if link.has_key('href'):
				links.append(link['href'])
		return links

	def indexURL(self,page):
		return self.indexBaseURL+"residential_r4.aspx?&CurrentPage="+str(page)	

	def mlsFromPosting(self,content):
		soup = BeautifulSoup(content)
		description = soup.find('td', {"class":"REMSListingDescription"}).content	

		mls = ""
		tableTwos = soup.findAll('table', {'class':'PropDetailsList'})
		for table in tableTwos:
			tds = table.findAll('td')
			if len(tds) is 2:
				key = tds[0].text.replace('&nbsp;','')
				val = tds[1].text.replace('&nbsp;','')
				#print key+" -> "+val
				if 'MLS' in key:
					mls = val
		if mls is not "":
			return mls
		return "no_mls"


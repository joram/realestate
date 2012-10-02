import os
import urllib
import userAgent
import time
from BeautifulSoup import BeautifulSoup          # For processing HTML
from urllib import FancyURLopener
import datetime
from datetime import datetime

class century21Details():
	def domain(self):
		return "century21"

	indexBaseURL = "http://www.century21.ca"
	
	def indexURL(self,page):
		return self.indexBaseURL+"/CA/BC/Victoria/0-/Page"+str(page)	

	def allInfoLinks(self, content):
		links = []
		soup = BeautifulSoup(content)
		linkData = soup.findAll('tr')
		for link in linkData:
			if link.has_key('onclick') and "location.href='/Property/BC/" in link['onclick']:
				detailsURL = link['onclick'].replace("location.href=","").replace("'","")
				links.append(detailsURL)
		links = list(set(links))
		return links


	def mlsFromPosting(self,content):
		soup = BeautifulSoup(content)
		mlsTR = soup.find('tr', {"id":"IDXRow"})

		if mlsTR:
			tds = mlsTR.findChildren()
			if len(tds)==2:
				mls = str(tds[1].text)
				if mls!="n/a":
					return mls
		return "no_mls"

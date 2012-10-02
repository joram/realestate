import os
import urllib
import userAgent
import time
from BeautifulSoup import BeautifulSoup          # For processing HTML
from urllib import FancyURLopener
import datetime
from datetime import datetime

class pHolmesDetails():
	def domain(self):
		return "pembertonHolmes"

	indexBaseURL = "http://www.pembertonholmes.com"
	
	def indexURL(self,page):
		return self.indexBaseURL+"/officelistings.html/SearchResults.form?_pg="+str(page)	

	def allInfoLinks(self, content):
		links = []
		soup = BeautifulSoup(content)
		allLinks = soup.findAll('a')
		for link in allLinks:
			if link.has_key('href') and "officelistings.html/details" in link['href']:
				detailsURL = link['href']
				links.append("/"+detailsURL)
		links = list(set(links))
		return links


	def mlsFromPosting(self,content):

		soup = BeautifulSoup(content)
		summarySection = soup.find('dl', {"class":'summary-line mls-num-line'})
		mlsRows = summarySection.findChildren()
		if len(mlsRows)==2 :
			mls = str(mlsRows[1].text)
			return mls
		return "no_mls"

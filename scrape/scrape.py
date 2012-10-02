import os
import urllib
import userAgent
import time
from BeautifulSoup import BeautifulSoup          # For processing HTML
from urllib import FancyURLopener
import datetime
from datetime import datetime

from detailsRemax           import remaxDetails
from detailsDFH             import dfhDetails
from detailsSutton          import suttonDetails
from detailsCentury21       import century21Details
from detailsPembertonHolmes import pHolmesDetails

class urlRandomUserAgent(FancyURLopener):
        agent = userAgent.randomUserAgent()

class scraper():

	def currentDir(self, info):
		domain = info.domain()

		# ./data
		if( "data" not in os.listdir(".")):
			os.mkdir("./data")

		# ./data/domain
		if( domain not in os.listdir("./data/")):
			os.mkdir("./data/"+info.domain())

		# ./data/domain/date
		curr=datetime.date(datetime.now())
		Year,WeekNum,DOW = curr.isocalendar()
		date = str(Year)+"_"+str(WeekNum) 
		if( date not in os.listdir("./data/"+info.domain()+"/")):
			os.mkdir("./data/"+info.domain()+"/"+date)

		s = "./data/"+info.domain()+"/"+date+"/"
		return s


	def fetchPage(self, url, filepath):
		fetcher = urlRandomUserAgent()
	        #print "fetching website now."
		#print "\tuser agent:",fetcher.agent
		#print "\tfile path:",filepath
		#print "\turl:",url
		print "fetching:",url

	        content = fetcher.open(url).read()
	        fh = open(filepath, "w")
	        fh.write(content)
	        fh.close()
	        return content
			
	
	def indexFile(self,page):
		return "index_"+str(page)+".html"

	

	def fetchNextIndex(self,info):

		currDir = self.currentDir(info)
		
		# find current page
		page = 0
		while self.indexFile(page) in os.listdir(currDir):
			page = page+1
		
		currIndexFile = currDir+self.indexFile(page)
		currIndexURL = info.indexURL(page)
		
		return self.fetchPage(currIndexURL, currIndexFile)

	def fetchPosting(self,link,info):
		url = info.indexBaseURL+link
		content = self.fetchPage(url,"tmp")

		mls = info.mlsFromPosting(content)
		mlsFilename = self.currentDir(info)+"MLS_"+mls+".html"
		os.rename('tmp',mlsFilename)
		

	def scrapeNextIndexAndPostings(self,info):
		# get index page
		indexContent = self.fetchNextIndex(info)
		# all posting details
		postingLinks = info.allInfoLinks(indexContent)
		for link in postingLinks:
			self.fetchPosting(link,info)
			time.sleep(1)

	def fetchNextPosting(self):
		return


	def scrape(self, realtorDetails):
		for details in realtorDetails:
			print "scraping:", details.domain()
			self.scrapeNextIndexAndPostings(details)



s = scraper()
realtorDetails = []
realtorDetails.append( remaxDetails() )
realtorDetails.append( dfhDetails() )
realtorDetails.append( suttonDetails() )
realtorDetails.append( century21Details() )
realtorDetails.append( pHolmesDetails() )
s.scrape(realtorDetails)



import os
from BeautifulSoup import BeautifulSoup
from geopy import geocoders  

def decomposeRemaxData(content):
	data = []
	soup = BeautifulSoup(content)

	# description
	descTD = soup.find('td', {"class":"REMSListingDescription"})
	if descTD:
		description = descTD.text
		data.append(['description',description])
	
	# address, price, bedrooms, bathrooms, living area, mls
	addrTD = soup.find('td', {'id':"MainListinTD"})
	if addrTD:
		tdContent = addrTD.prettify()
		propDetailsSoup = BeautifulSoup(tdContent)
		tds = propDetailsSoup.findAll('td', {'class':'REMSListingCaption'})
		if len(tds)>=1:
			addr = tds[0].text
			data.append(['address',addr])
			


	# details
	tableTwos = soup.findAll('table', {'class':'PropDetailsList'})
	for table in tableTwos:
		tds = table.findAll('td')
		if len(tds) is 2:
			key = tds[0].text.replace('&nbsp;','')
			val = tds[1].text.replace('&nbsp;','')
			data.append([key,val])

	return data


def remax(csvFH):
	baseFolder = "./data/remax/"
	for folder in os.listdir(baseFolder):
		folder = baseFolder+"/"+folder
		g = geocoders.Google()
		print folder
		for dataFile in os.listdir(folder):
			dataFile = folder+"/"+dataFile
			content = open(dataFile, "r").read()		
			data = decomposeRemaxData(content)
			price = 0
			lat = 0
			lng = 0
			for line in data:
				key = line[0]
				val = line[1]
	#			print key,"\t:\t",val
				if(key=="address"):
					try:
						place, (lat, lng) = g.geocode(val)  
					except:
						#print "error parsing location: "+val
						lat = 0
						lng = 0
	
				if key=="Price":
					price = val.strip("$").strip(" ")
			
			if price!=0 and lat!=0 and lng!=0 :
				csvLine = str(price)
				csvLine = csvLine.replace(',',"")
				csvLine = csvLine+","+str(lat)+","+str(lng)
				print csvLine
				csvFH.write(csvLine+"\n")
	print "done remax"

def decomposeDfhData(content):
	data = []
	soup = BeautifulSoup(content)
	dataBlock = soup.find("td", {"class":"colorbar"})
	if data != 'NoneType':
		soup2 = BeautifulSoup(dataBlock.prettify())
		fonts = soup2.findAll('font',{'size':'2'})
		if len(fonts)>=1 :
			parts = fonts[0].text.split("-")
			if len(parts)>=1:
				data.append(['address',parts[0]])
			if len(parts)>=3:
				data.append(['price',parts[2].replace(' ','').replace('$','').replace(",",'').replace("\n",'')])
	return data

def dfh(csvFH):
	baseFolder = "./data/dfh/"
	for folder in os.listdir(baseFolder):
		folder = baseFolder+"/"+folder
		g = geocoders.Google()
		print folder
		for dataFile in os.listdir(folder):
			dataFile = folder+"/"+dataFile
			content = open(dataFile, "r").read()		
			data = decomposeDfhData(content)
			price = 0
			lat = 0
			lng = 0
			for line in data:
				key = line[0]
				val = line[1]
	#			print key,"\t:\t",val
				if(key=="address"):
					try:
						place, (lat, lng) = g.geocode(val)  
					except:
						#print "error parsing location: "+val
						lat = 0
						lng = 0
	
				if key=="price":
					price = val.strip("$").strip(" ")
			
			if price!=0 and lat!=0 and lng!=0 :
				csvLine = str(price)
				csvLine = csvLine.replace(',',"")
				csvLine = csvLine+","+str(lat)+","+str(lng)
				print csvLine
				csvFH.write(csvLine+"\n")
	print "done dfh"

csvFile = "/var/www/heatmap/priceData.csv"
csvFH = open(csvFile,"w")
remax(csvFH)
dfh(csvFH)
csvFH.close()

from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os
import json
from pprint import pprint

def get_soup(url,header):
  return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)))

def getimageurl(search):
	image_type = "Action"
	query = search
	query= query.split()
	query='+'.join(query)
	url=url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
	header = {'User-Agent': 'Mozilla/5.0'} 
	soup = get_soup(url,header)

	images = [a['src'] for a in soup.find_all("img", {"src": re.compile("gstatic.com")})]
	return images[0]

with open('mpresults.json') as json_data:
	d=json.load(json_data)
	for mps in d:
		searh=mps['first_name']+' '+ mps['last_name']
		url=getimageurl(searh)
		mps["imgurl"]=url

with open('mps.json','w') as outfile:
	json.dump(d,outfile,indent=2)

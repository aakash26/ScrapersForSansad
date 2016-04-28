from lxml import etree
import requests
import time
import urllib2
import mechanize
from bs4 import BeautifulSoup
import re
import string
import json
from string import whitespace

url="http://www.prsindia.org/mptrack/"

f=open("MP.csv","r")
d=f.read().split("\n")
d=d[1:]

mainjson=[]
for each in d:
	try:
		url="http://www.prsindia.org/mptrack/"
		json={}
		data=str(each).split(",")
		name=data[0]
		json["name"]=name
		name=name.replace(" ","")
		name=name.replace(".","")
		br = mechanize.Browser() 
		br.set_handle_robots(False)
		url=url+name+'/'
		html=br.open(url).read()
		soup = BeautifulSoup(html)
		questions={}
		debates={}
		dbtitle=[]
		dbtype=[]
		qutitle=[]
		qutype=[]
		
		for row in soup('table', {'id': 'myTable2'})[0].tbody('tr'):
			try:
				dbtitle.append(row.findAll('td')[1].text.strip())
				dbtype.append(row.findAll('td')[2].text.strip())
			except:
				pass

		for row in soup('table', {'id': 'myTable1'})[0].tbody('tr'):
			try:
				qutitle.append(row.findAll('td')[1].text.strip())
				qutype.append(row.findAll('td')[3].text.strip())
			except:
				pass
		debates["debatetitle"]=dbtitle
		debates["debatestpye"]=dbtype
		questions["questionstitle"]=qutitle
		questions["questionsministry"]=qutype
		json["debates"]=debates
		json["questions"]=questions
		mainjson.append(json)
	except:
		pass
print mainjson


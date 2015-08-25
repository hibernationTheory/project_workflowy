from contextlib import closing
import cookielib
import httplib
import json
import os
import urllib2
import time

import requests

from bs4 import BeautifulSoup as bs

path = "https://workflowy.com/s/WpZtYcaBPq"
r = requests.get(path, stream=True)

headers = r.headers
content_length = headers.get('content-length', None)

counter = 0
if content_length:
	while int(content_length) >= 51351 and counter < 10:
		time.sleep(0.5)
		counter += 1
		headers = r.headers
		content_length = headers.get('content-length', None)
	print(counter)
	print(r.content)

#with closing(requests.get('path', stream=True)) as r:

#	headers = r.headers
#	print(headers)

#time.sleep(9)
#print(dir(r))

"""
content_length = headers.get('content-length', None)
if content_length:
	while int(content_length) >= 51351:
"""




#print(r.content)



"""
r = requests.get(path, stream=True)
headers = r.headers
content_length = headers.get('content-length', None)
time.sleep(2)


print(r.content)


#print(dir(r))
#print(r.headers)
#print(r.request.headers)
#print(r.content)
"""

"""
req = urllib2.Request(path)
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
resp = opener.open(req)
time.sleep(2)

read = resp.read()
time.sleep(2)
read = resp.read()

print(read)
"""

#soup = bs(page)


"""
page = urllib2.urlopen(path)

mainTreeRoot = soup.find("div", {"class":"mainTreeRoot"})
print(mainTreeRoot)
"""




"""
try:
    page = urllib2.urlopen(path)
    soup = beaSoup(page)
    
    target_div  = soup.findAll("div", {"class":"data_box"})
    target_links = []

    for div in target_div:
        link = div.find("a", {"class":"no_underline"})
        target_links.append(link)

    for link in target_links:
        dataList.append((link.text, link["href"]))
except Exception as e:
    print e
time.sleep(0.5)

return dataList


"""